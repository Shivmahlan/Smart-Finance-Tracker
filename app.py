import streamlit as st
import pandas as pd
import os
from datetime import datetime
from io import BytesIO
try:
    from fpdf import FPDF
    FPDF_AVAILABLE = True
except ImportError:
    FPDF_AVAILABLE = False

# --- Data Loading and Saving ---
EXPENSE_FILE = 'expenses.csv'
INVESTMENT_FILE = 'investments.csv'
BUDGET_FILE = 'budget.txt'

# Helper functions
def load_data(file_path, is_investment=False):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        if not is_investment and 'payment_type' not in df.columns:
            df['payment_type'] = 'Other'
        return df
    columns = ["timestamp", "category", "amount"]
    if not is_investment:
        columns.append("payment_type")
    return pd.DataFrame(columns=columns)

def save_data(df, file_path):
    df.to_csv(file_path, index=False)

def load_budget():
    if os.path.exists(BUDGET_FILE):
        try:
            with open(BUDGET_FILE, 'r') as f:
                return float(f.read())
        except Exception:
            return 0
    return 0

def save_budget(amount):
    with open(BUDGET_FILE, 'w') as f:
        f.write(str(amount))

def get_monthly_summary_data(expenses, budget):
    if expenses.empty:
        return None
    expenses['timestamp'] = pd.to_datetime(expenses['timestamp'])
    now = datetime.now()
    monthly_df = expenses[(expenses['timestamp'].dt.month == now.month) & (expenses['timestamp'].dt.year == now.year)]
    if monthly_df.empty:
        return None
    total_spent = monthly_df['amount'].sum()
    category_summary = monthly_df.groupby("category")['amount'].sum().reset_index()
    category_summary['percentage'] = (category_summary['amount'] / total_spent * 100).round(2)
    type_summary = monthly_df.groupby('payment_type')['amount'].sum()
    upi_total = type_summary.get('UPI', 0)
    other_total = type_summary.get('Other', 0)
    savings = budget - total_spent if budget > 0 else 0
    return {
        "month_name": now.strftime('%B %Y'),
        "category_summary": category_summary,
        "total_spent": total_spent,
        "upi_total": upi_total,
        "other_total": other_total,
        "budget": budget,
        "savings": savings
    }

def generate_pdf_report(data):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 18)
    pdf.cell(0, 10, f"Expense Report - {data['month_name']}", 0, 1, 'C')
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Overall Summary", 0, 1)
    pdf.set_font("Arial", '', 12)
    summary_items = [
        ["Total Spent:", f"Rs. {data['total_spent']:.2f}"],
        ["Monthly Budget:", f"Rs. {data['budget']:.2f}" if data['budget'] > 0 else "Not set"],
        ["Total Savings:" if data['savings'] >= 0 else "Amount Overspent:", f"Rs. {abs(data['savings']):.2f}"]
    ]
    for item in summary_items:
        pdf.cell(50, 8, item[0], 0, 0)
        pdf.cell(0, 8, item[1], 0, 1)
    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(0, 10, "Spending by Category", 0, 1)
    pdf.set_font("Arial", 'B', 10)
    pdf.cell(80, 8, "Category", 1, 0, 'C')
    pdf.cell(50, 8, "Amount (Rs.)", 1, 0, 'C')
    pdf.cell(40, 8, "Percentage (%)", 1, 1, 'C')
    pdf.set_font("Arial", '', 10)
    for _, row in data['category_summary'].iterrows():
        pdf.cell(80, 8, str(row['category']), 1, 0)
        pdf.cell(50, 8, f"{row['amount']:.2f}", 1, 0, 'R')
        pdf.cell(40, 8, f"{row['percentage']:.2f}", 1, 1, 'R')
    output = BytesIO()
    pdf.output(output)
    output.seek(0)
    return output

# --- Streamlit UI ---
st.set_page_config(page_title="Expense Management System", layout="centered")
st.title("💸 Expense Management System")


# Load data
expenses = load_data(EXPENSE_FILE)
investments = load_data(INVESTMENT_FILE, is_investment=True)
budget = load_budget()

# --- Dashboard Sections ---
with st.expander("➕ Add Expense", expanded=True):
    with st.form("expense_form"):
        category = st.text_input("Category", "Food")
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        payment_type = st.selectbox("Payment Type", ["Cash", "UPI", "Credit Card", "Debit Card"])
        submitted = st.form_submit_button("Add Expense")
        if submitted and amount > 0:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = {"timestamp": timestamp, "category": category, "amount": amount, "payment_type": payment_type}
            expenses = pd.concat([expenses, pd.DataFrame([new_row])], ignore_index=True)
            save_data(expenses, EXPENSE_FILE)
            st.success(f"Added {amount} in {category} ({payment_type})")

with st.expander("💹 Add Investment", expanded=False):
    with st.form("investment_form"):
        category = st.text_input("Investment Category", "Stocks")
        amount = st.number_input("Investment Amount", min_value=0.0, step=0.01)
        submitted = st.form_submit_button("Add Investment")
        if submitted and amount > 0:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            new_row = {"timestamp": timestamp, "category": category, "amount": amount}
            investments = pd.concat([investments, pd.DataFrame([new_row])], ignore_index=True)
            save_data(investments, INVESTMENT_FILE)
            st.success(f"Added investment of {amount} in {category}")

with st.expander("📊 Monthly Expense Summary", expanded=False):
    if expenses.empty:
        st.info("No expenses recorded for this month.")
    else:
        summary = get_monthly_summary_data(expenses, budget)
        if not summary:
            st.info("No expenses recorded for this month.")
        else:
            st.subheader(f"Summary for {summary['month_name']}")
            st.write("### Spending by Category")
            st.dataframe(summary['category_summary'])
            st.write("### Spending by Payment Type")
            st.write(f"UPI Payments: ₹{summary['upi_total']:.2f}")
            st.write(f"Other Expenses: ₹{summary['other_total']:.2f}")
            st.write(f"**Total Spent:** ₹{summary['total_spent']:.2f}")
            st.write(f"**Budget:** ₹{summary['budget']:.2f}" if summary['budget'] > 0 else "**Budget:** Not set")
            if summary['budget'] > 0:
                if summary['savings'] >= 0:
                    st.success(f"Money Saved: ₹{summary['savings']:.2f}")
                else:
                    st.error(f"Money Overspent: ₹{-summary['savings']:.2f}")

with st.expander("📈 Investment Summary", expanded=False):
    if investments.empty:
        st.info("No investments recorded yet.")
    else:
        total_invested = investments['amount'].sum()
        summary = investments.groupby('category')['amount'].sum().sort_values(ascending=False)
        st.write("### Investment by Category")
        st.dataframe(summary.reset_index())
        st.write(f"**Total Invested:** ₹{total_invested:.2f}")

with st.expander("🎯 Set/Change Budget", expanded=False):
    budget_float = float(budget) if budget is not None else 0.0
    with st.form("budget_form"):
        new_budget = st.number_input("Monthly Budget", min_value=0.0, step=0.01, value=budget_float)
        submitted = st.form_submit_button("Set Budget")
        if submitted:
            save_budget(float(new_budget))
            st.success(f"Budget set to ₹{float(new_budget):.2f}")

with st.expander("🗑️ List & Delete Expense", expanded=False):
    if expenses.empty:
        st.info("No expenses to display.")
    else:
        st.dataframe(expenses)
        idx = st.number_input("Enter the index of the expense to delete (row number)", min_value=0, max_value=len(expenses)-1, step=1)
        if st.button("Delete Expense"):
            expenses = expenses.drop(expenses.index[idx]).reset_index(drop=True)
            save_data(expenses, EXPENSE_FILE)
            st.success(f"Deleted expense at index {idx}")

with st.expander("💥 Clear All Expenses", expanded=False):
    if st.button("Delete ALL Expenses"):
        expenses = pd.DataFrame(columns=["timestamp", "category", "amount", "payment_type"])
        save_data(expenses, EXPENSE_FILE)
        st.success("All expenses have been cleared.")

with st.expander("📄 Generate PDF Report", expanded=False):
    if not FPDF_AVAILABLE:
        st.error("FPDF library not installed. Please run: pip install fpdf2")
    else:
        summary = get_monthly_summary_data(expenses, budget)
        if not summary:
            st.info("No expenses to report for this month.")
        else:
            if st.button("Generate PDF Report"):
                pdf_bytes = generate_pdf_report(summary)
                st.success("PDF report generated!")
                st.download_button(
                    label="Download PDF",
                    data=pdf_bytes,
                    file_name=f"Expense_Report_{datetime.now().strftime('%B_%Y')}.pdf",
                    mime="application/pdf"
                )

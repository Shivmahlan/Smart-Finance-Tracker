# 💰 Smart Finance Tracker

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**Track expenses. Set budgets. Generate reports. All from Python.**

*Expense logging · Budget monitoring · PDF & CSV export · Spending analytics*

</div>

---

## 📸 Demo

> 🎥 *Screenshot / GIF of the dashboard coming soon*

---

## ✨ What Is This?

**Smart Finance Tracker** is a Python-based personal finance management tool that helps you log daily expenses, monitor budgets, visualize spending trends, and export detailed reports — all from a simple script.

Built as a practical data analytics project, it demonstrates real-world use of Python for financial data processing, reporting, and visualization.

---

## 🎯 Features

| Feature | Description |
|---|---|
| 📝 **Expense Logging** | Record daily transactions with category, amount, and date |
| 🎯 **Budget Management** | Set monthly/custom budgets and track against real spending |
| 📊 **Spending Analytics** | Visualize trends — category-wise, monthly, over time |
| 📄 **PDF Export** | Auto-generate formatted expense reports (like the Sep 2025 sample) |
| 📁 **CSV Export** | Export raw data for use in Excel / Google Sheets |
| 🧪 **Test Coverage** | Automated test cases to validate core logic |

---

## 🧠 How It Works

```
┌──────────────────────────────────────────────────────────────────┐
│                  SMART FINANCE TRACKER PIPELINE                  │
└──────────────────────────────────────────────────────────────────┘

  👤 User Input
       │
       ▼
  ┌──────────────┐
  │   app.py     │  ← Main entry point, handles user interaction
  └──────┬───────┘
         │
         ▼
  ┌──────────────┐         ┌─────────────────┐
  │ finanace.py  │ ──────► │  expenses.csv   │
  │ Core Logic   │         │  (data storage) │
  └──────┬───────┘         └─────────────────┘
         │
         ├──── Budget Check ──────► budget.txt
         │
         ├──── Analysis ─────────► Pandas + Matplotlib
         │                         (charts & trends)
         │
         └──── Export ───────────► PDF Report / CSV
                                   e.g. Expense_Report_September_2025.pdf
```

---

## 📂 Project Structure

```
Smart-Finance-Tracker/
│
├── 📄 app.py                              ← Main application entry point
├── 📄 finanace.py                         ← Core financial logic & operations
│
├── 📊 expenses.csv                        ← Expense data storage
├── 📝 budget.txt                          ← User-defined budget config
│
├── 📋 Expense_Report_September_2025.pdf   ← Sample exported report
│
├── 🧪 testcase44.py                       ← Automated test scenarios
├── 📦 requirements.txt                    ← Python dependencies
└── 📖 README.md
```

---

## 🛠️ Tech Stack

```
┌─────────────────┬──────────────────────────────────────────────────┐
│  Library        │  Role                                            │
├─────────────────┼──────────────────────────────────────────────────┤
│  Python 3.x     │  Core application logic                          │
│  Pandas         │  Expense data loading, filtering, aggregation    │
│  Matplotlib     │  Spending trend charts & visualizations          │
│  ReportLab      │  PDF report generation                           │
│  CSV (built-in) │  Lightweight expense data storage & export       │
└─────────────────┴──────────────────────────────────────────────────┘
```

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/Shivmahlan/Smart-Finance-Tracker.git
cd Smart-Finance-Tracker
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
python app.py
```

---

## ⚙️ Configuration

**Set your budget** — edit `budget.txt`:

```
monthly_budget=10000
food=3000
transport=1500
entertainment=1000
utilities=2000
```

**Expense format** — `expenses.csv` follows this schema:

```
date,category,description,amount
2025-09-01,Food,Groceries,450
2025-09-02,Transport,Uber,120
2025-09-03,Entertainment,Netflix,199
```

---

## 📊 Sample Report

A sample exported report is included in the repo:
👉 [`Expense_Report_September_2025.pdf`](./Expense_Report_September_2025.pdf)

It shows:
- Total spend vs budget
- Category-wise breakdown
- Daily spending trend

---

## 🗺️ Roadmap

- [x] Expense logging via CSV
- [x] Budget setting & tracking
- [x] PDF report generation
- [x] CSV export
- [ ] Interactive CLI menu
- [ ] Monthly comparison charts
- [ ] Email report delivery
- [ ] SQLite database backend (replace CSV)
- [ ] Web dashboard (Flask / Streamlit)

---

## 🧪 Running Tests

```bash
python testcase44.py
```

Tests cover core financial logic — budget calculations, expense categorization, and report generation.

---

## 🤝 Contributing

Pull requests are welcome! For major changes, open an issue first.

1. Fork the repo
2. Create a branch: `git checkout -b feature/your-feature`
3. Commit: `git commit -m "Add your feature"`
4. Push: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 👨‍💻 Author

**Shiv Mahlan**
B.Tech CSE (Data Science) · Ch. Devi Lal University 

[![GitHub](https://img.shields.io/badge/GitHub-Shivmahlan-181717?style=flat-square&logo=github)](https://github.com/Shivmahlan)

---

## 📄 License

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.

---

<div align="center">

*Built to make personal finance less painful* 💸

⭐ Star this repo if it helped you!

</div>

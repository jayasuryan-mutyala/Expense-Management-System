#  Expense Management System

A full-stack **Expense Management System** built with **FastAPI** (backend) and **Streamlit** (frontend) that allows users to track daily expenses and analyze spending through interactive analytics.

---

##  Features

- Add and update daily expenses
- View expenses by date
- Analyze expenses over a date range
- Monthly expense analytics
- Category-wise expense comparison (bar charts)
- Clean REST API with FastAPI
- Interactive dashboard using Streamlit
- Centralized logging
- Environment-based configuration

---

##  Tech Stack

**Backend**
- FastAPI
- MySQL
- Pydantic
- Uvicorn

**Frontend**
- Streamlit
- Pandas

**Other**
- Conda (environment management)
- Pytest (testing)
- Logging
- Git

---

##  Project Structure

```text
EXPENSE_MANAGER/
│
├── backend/                  # FastAPI backend (API + database logic)
│   ├── __init__.py           # Marks backend as a Python package
│   ├── db_helper.py          # Database access layer (SQL queries, connections)
│   ├── logging_setup.py      # Centralized logging configuration
│   └── server.py             # FastAPI app and API route definitions
│
├── frontend/                 # Streamlit frontend (UI layer)
│   ├── __init__.py           # Marks frontend as a Python package
│   ├── app.py                # Streamlit entry point (tabs & layout)
│   ├── add_update_ui.py      # Add / update daily expenses UI
│   ├── analytics_ui.py       # Date-range analytics UI
│   ├── analytics_months_ui.py# Monthly expense analytics UI
│   └── category_analytics_ui.py # Category-wise expense comparison UI
│
├── logs/                     # Application logs
│   └── server.log            # Backend runtime logs
│
├── tests/                    # Automated tests
│   ├── backend/              # Backend unit & integration tests
│   └── frontend/             # Frontend/UI tests (if added later)
│
├── .env                      # Environment variables (DB creds, secrets)
├── .gitignore                # Git ignored files & folders
├── .python-version           # Python version pinning
├── conftest.py               # Pytest global fixtures
├── environment.yml           # Conda environment definition
├── pyproject.toml            # Project metadata & dependencies
├── uv.lock                   # Locked dependency versions (uv)
├── main.py                   # Optional entry point / experiments
└── README.md                 # Project documentation
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/jayasuryan-mutyala/Expense-Management-System
cd Expense-Management-System
```

---

### 2️⃣ Create Conda virtual environment
```bash
conda env create -f environment.yml
conda activate expense_env
```

---

### 3️⃣ Configure environment variables
Create a `.env` file in the project root:

```env
DB_HOST=localhost
DB_NAME=expense_manager
DB_USER=root
DB_PASSWORD=your_password
```

---

### 4️⃣ Run the FastAPI backend
```bash
uvicorn backend.server:app --reload
```

Backend will be available at:
```
http://127.0.0.1:8000
```

---

### 5️⃣ Run the Streamlit frontend
```bash
streamlit run frontend/app.py
```

Frontend will be available at:
```
http://localhost:8501
```

---

## 🧪 Running Tests

```bash
pytest
```

---

## 📝 Logging

Logs are written to:
```
logs/server.log
```

---



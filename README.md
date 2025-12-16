# Expense Management System

This project is an expense management system that consists of a streamlit frontend and FastAPI backend server.


## Project structure
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


## Setup Instructions

1. **Clone the repository**:
'''bash
git clone https:github.com/jayasuryan-mutyala/Expense-Management-System

cd expense-management-system
'''

1. **Install conda virtual environment**
'''commandline
conda env create -f environment.yml
'''

1. **Run FastAPI server**
'''commandline
uvicorn backend.server:app --reload
'''

1. **Run Streamlit app:
'''commandline 
streamlit run frontend/app.py
'''
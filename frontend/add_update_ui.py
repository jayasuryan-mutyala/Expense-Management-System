import streamlit as st
from datetime import datetime 
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

def add_update_tab():
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    date_key = selected_date.isoformat()

    response = requests.get(f"{API_URL}/expenses/{selected_date}")
    existing_expenses = response.json() if response.status_code == 200 else []

    @st.cache_data
    def fetch_categories():
        r = requests.get(f"{API_URL}/categories/")
        if r.status_code != 200:
            return []
        return [item["category"] for item in r.json()]

    categories = fetch_categories()

    if not categories:
        st.warning("No categories available")
        return

    with st.form(key=f"expense_form_{date_key}"):
        expenses = []

        for i in range(5):
            if i < len(existing_expenses):
                amount = existing_expenses[i]["amount"]
                category = existing_expenses[i]["category"]
                notes = existing_expenses[i]["notes"]
            else:
                amount = 0.0
                category = categories[0]
                notes = ""

            category_index = categories.index(category) if category in categories else 0

            col1, col2, col3 = st.columns(3)

            with col1:
                amount_input = st.number_input(
                    "Amount",
                    min_value=0.0,
                    value=amount,
                    key=f"{date_key}_amount_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                category_input = st.selectbox(
                    "Category",
                    categories,
                    index=category_index,
                    key=f"{date_key}_category_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    "Notes",
                    value=notes,
                    key=f"{date_key}_notes_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        if st.form_submit_button("Save"):
            payload = [e for e in expenses if e["amount"] > 0]
            r = requests.post(f"{API_URL}/expenses/{selected_date}", json=payload)

            if r.status_code == 200:
                st.success("Expense updated successfully")
            else:
                st.error("Failed to update expenses")

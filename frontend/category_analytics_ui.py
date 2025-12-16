import streamlit as st 
import pandas as pd 
import requests 

API_URL = "http://localhost:8000"

def category_analytics_tab():
    st.subheader("Expense Breakdown by Category")

    response = requests.get(f"{API_URL}/category_expense")

    if response.status_code != 200:
        st.error("Failed to fetch category expenses data")
        return
    
    data = response.json()

    if not data:
        st.info("No expense data available")
        return 
    
    df = pd.DataFrame(data)

    total = df['total_expense'].sum()
    df['percentage'] = (df['total_expense']/total) * 100 if total else 0

    st.bar_chart(df.set_index("category")['total_expense'],
                 use_container_width=True)
    st.table(
        df.style.format({
            "total_expense": "{:.2f}",
            "percentage": "{:.2f}%"
        })
    )

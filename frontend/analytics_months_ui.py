import streamlit as st
import pandas as pd 
import requests 

API_URL = 'http://localhost:8000'

def analytics_by_month_tab():
    st.subheader("Expense Breakdown by Months")

    response = requests.get(f"{API_URL}/monthly_expense")

    if response.status_code != 200:
        st.error("Failed to fetch month wise expenses")
        return 
    
    data = response.json()

    if not data:
        st.info("No expense data available")
        return 
    
    df = pd.DataFrame(data)

    st.bar_chart(
        data=df.set_index("month")['total_expense'],
        use_container_width=True
    )

    st.table(df)
import streamlit as st
from datetime import datetime 
import requests
import pandas as pd 


API_URL = "http://localhost:8000"


def analytics_tab():
    col1,col2 = st.columns(2)
    with col1:
        start_date = st.date_input(label="Start Date",
                               value=datetime(2024,8,1))
    with col2:
        end_date = st.date_input(label="End Date",
                               value=datetime(2024,8,1))
    
    if st.button("Get Analytics"):
        payload = {
            "start_date":start_date.strftime("%Y-%m-%d"),
            "end_date":end_date.strftime("%Y-%m-%d"),
        }

        response = requests.post(f"{API_URL}/analytics/",json=payload)
        
        if response.status_code != 200:
            st.error("Failed to fetch data")
            return
        
        items = response.json()['items']

        df = pd.DataFrame(items)

        if df.empty:
            st.info("No analytics available")
            return

        df_sorted = df.sort_values(by='percentage',ascending=False)

        st.bar_chart(data=df_sorted.set_index("category")["percentage"],
                     use_container_width=True)

        st.table(
            df_sorted.style.format({
                "total":"{:.2f}",
                "percentage":"{:.2f}%",
            })
        )

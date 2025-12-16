import streamlit as st 
from datetime import datetime 
import requests
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab
from analytics_months_ui import analytics_by_month_tab
from category_analytics_ui import category_analytics_tab

# Note do not use streamlit url here 
# USE FASTAPI
API_URL = "http://localhost:8000"

st.title("Expense Tracking System")

tab1,tab2,tab3,tab4 = st.tabs(["Add/Update","Analytics","Analytics By Months","Analytics By Category"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

with tab3:
    analytics_by_month_tab()

with tab4:
    category_analytics_tab()
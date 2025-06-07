# app.py

import streamlit as st
from src.data_loader import load_data
from src.kpis import calculate_kpis
from src.visuals import sales_by_region, age_distribution, gender_pie
from src.insights import generate_insight
from src.ui import inject_css, render_kpis

st.set_page_config(page_title="SME BI Dashboard", layout="wide")

inject_css()

st.title("SME Business Intelligence Dashboard (Malawi)")
st.markdown("Empowering SME owners in Malawi with clear, actionable data.")

# Load data
df = load_data()

# Calculate KPIs
kpis = calculate_kpis(df)

# Show KPIs section
st.subheader("Key Performance Indicators")
render_kpis(kpis)

# Business insight section
st.subheader("Business Insight")
st.info(generate_insight(df))

# Layout for charts
col1, col2 = st.columns([2, 1])

with col1:
    st.plotly_chart(sales_by_region(df), use_container_width=True)

with col2:
    st.plotly_chart(gender_pie(df), use_container_width=True)

st.subheader("Customer Age Distribution")
st.plotly_chart(age_distribution(df), use_container_width=True)

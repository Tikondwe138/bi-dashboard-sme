# src/dashboard.py

import streamlit as st
from src.data_loader import load_data
from src.kpis import calculate_kpis
from src.visuals import sales_by_region, age_distribution, gender_pie
from src.insights import generate_insight
from src.localization import format_currency, t
from src.ui import inject_css

def run_dashboard():
    st.set_page_config(page_title="BI Dashboard - SMEs Malawi", layout="wide")
    inject_css()

    st.title("SME Business Intelligence Dashboard (Malawi)")
    st.markdown("Visualize trends, monitor KPIs, and get data-driven insights.")

    try:
        df = load_data()
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return

    # KPIs
    st.header(t("total_sales"))
    kpis = calculate_kpis(df)
    col1, col2, col3 = st.columns(3)
    col1.metric(t("total_sales"), format_currency(kpis["Total Sales"]))
    col2.metric(t("total_profit"), format_currency(kpis["Total Profit"]))
    col3.metric(t("profit_margin"), f"{kpis['Profit Margin (%)']:.2f}%")

    # Charts
    st.header(t("region_sales"))
    st.plotly_chart(sales_by_region(df), use_container_width=True)

    st.header(t("customer_age"))
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(age_distribution(df), use_container_width=True)
    with col2:
        st.plotly_chart(gender_pie(df), use_container_width=True)

    # Insight
    st.header(t("insight_title"))
    st.info(generate_insight(df))

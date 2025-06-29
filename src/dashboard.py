# src/dashboard.py

import streamlit as st
from src.data_loader import load_data
from src.kpis import calculate_kpis
from src.visuals import sales_by_region, age_distribution, gender_pie
from src.insights import generate_insight
from src.ui import inject_css, render_kpis, section_header


def run_dashboard():
    st.set_page_config(page_title="SME BI Dashboard (Malawi)", layout="wide", initial_sidebar_state="expanded")
    inject_css()

    st.title("SME Business Intelligence Dashboard (Malawi)")
    st.markdown(
        "<span style='font-size:1.1rem;'>Visualize trends, monitor KPIs, and get data-driven insights for SMEs in Malawi.</span>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    try:
        df = load_data()
    except Exception as e:
        st.error(f"Failed to load data: {e}")
        return

    if df is None or df.empty:
        st.warning("No data available. Please check your data source.")
        return

    # KPIs
    section_header("Key Performance Indicators")
    render_kpis(calculate_kpis(df))
    st.markdown("---")

    # Regional Sales
    section_header("Regional Sales")
    st.plotly_chart(sales_by_region(df), use_container_width=True)
    st.markdown("---")

    # Customer Demographics
    section_header("Customer Demographics")
    col1, col2 = st.columns(2)
    with col1:
        st.plotly_chart(age_distribution(df), use_container_width=True)
    with col2:
        st.plotly_chart(gender_pie(df), use_container_width=True)
    st.markdown("---")

    # Business Insight
    section_header("Business Diagnosis")
    st.info(generate_insight(df))


if __name__ == "__main__":
    run_dashboard()

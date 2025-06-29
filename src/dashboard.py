# src/dashboard.py

import streamlit as st
from src.data_loader import load_data
from src.kpis import calculate_kpis
from src.visuals import sales_by_region, age_distribution, gender_pie
from src.insights import generate_insight
from src.ui import inject_css, render_kpis, section_header
import io
import pandas as pd


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

    # Sidebar filters
    regions = df['Region'].unique()
    products = df['Product'].unique()
    date_min, date_max = df['Date'].min(), df['Date'].max()

    with st.sidebar:
        selected_regions = st.multiselect("Filter by Region", regions, default=list(regions))
        selected_products = st.multiselect("Filter by Product", products, default=list(products))
        date_range = st.date_input("Date Range", [date_min, date_max])

    filtered_df = df[
        (df['Region'].isin(selected_regions)) &
        (df['Product'].isin(selected_products)) &
        (df['Date'] >= pd.to_datetime(date_range[0])) &
        (df['Date'] <= pd.to_datetime(date_range[1]))
    ]

    # KPIs
    section_header("Key Performance Indicators")
    render_kpis(calculate_kpis(filtered_df))
    st.markdown("---")

    # Regional Sales and Gender Distribution side by side
    section_header("Regional Sales & Gender Distribution")
    col1, col2 = st.columns([1.2, 1])
    with col1:
        fig_region = sales_by_region(filtered_df)
        fig_region.update_layout(
            autosize=False,
            width=520, height=340,
            margin=dict(l=10, r=10, t=40, b=10),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color="#222")
        )
        st.plotly_chart(fig_region, use_container_width=False)
    with col2:
        fig_gender = gender_pie(filtered_df)
        fig_gender.update_layout(
            autosize=False,
            width=340, height=340,
            margin=dict(l=10, r=10, t=40, b=10),
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color="#222")
        )
        st.plotly_chart(fig_gender, use_container_width=False)
    st.markdown("---")

    # Customer Age Distribution
    section_header("Customer Age Distribution")
    fig_age = age_distribution(filtered_df)
    fig_age.update_layout(
        autosize=False,
        width=860, height=320,
        margin=dict(l=10, r=10, t=40, b=10),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222")
    )
    st.plotly_chart(fig_age, use_container_width=False)
    st.markdown("---")

    # Business Insight
    section_header("Business Diagnosis")
    st.info(generate_insight(filtered_df))

    # Excel download for filtered data
    def to_excel(df):
        output = io.BytesIO()
        with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
            df.to_excel(writer, index=False, sheet_name='Sheet1')
        return output.getvalue()

    st.sidebar.download_button(
        label="Download Filtered Data as Excel",
        data=to_excel(filtered_df),
        file_name='filtered_data.xlsx',
        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )


if __name__ == "__main__":
    run_dashboard()

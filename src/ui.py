# src/ui.py

import streamlit as st
from src.localization import format_currency

def inject_css():
    """Inject custom CSS styles into Streamlit app."""
    try:
        with open("assets/styles.css") as f:
            css = f.read()
        st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found. Styling may be affected.")

def render_kpis(kpi_dict):
    """Render key performance indicators in three columns."""
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Sales", format_currency(kpi_dict.get("Total Sales", 0)))
    col2.metric("Total Profit", format_currency(kpi_dict.get("Total Profit", 0)))
    profit_margin = kpi_dict.get("Profit Margin (%)", 0)
    col3.metric("Profit Margin", f"{profit_margin:.2f}%")

def section_header(title: str):
    """Stylish section header."""
    st.markdown(f"""
        <h2 class='region-header'>{title}</h2>
        <hr style='border-top: 2px solid #ccc; margin-top: -10px;' />
    """, unsafe_allow_html=True)

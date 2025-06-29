import streamlit as st
from src.localization import format_currency

def inject_css():
    """Inject custom CSS for consistent app styling."""
    try:
        with open("assets/styles.css") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Custom CSS file not found. Styling may be affected.")

def render_kpis(kpi_dict):
    """Render KPIs inside a styled container."""
    with st.container():
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Sales", format_currency(kpi_dict.get("Total Sales", 0)))
        col2.metric("Total Profit", format_currency(kpi_dict.get("Total Profit", 0)))
        profit_margin = kpi_dict.get("Profit Margin (%)", 0)
        col3.metric("Profit Margin", f"{profit_margin:.2f}%")

def section_header(title: str):
    """Stylish section header consistent with CSS."""
    st.markdown(
        f"<div class='section-header'>{title}</div>"
        "<hr style='border-top: 1px solid #e0e0e0; margin-top: 0.25rem; margin-bottom: 1rem;' />",
        unsafe_allow_html=True
    )

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from src.data_loader import load_data
from src.kpis import calculate_kpis
from src.visuals import sales_by_region, age_distribution, gender_pie
from src.insights import generate_insight
from src.ui import inject_css, render_kpis
from src.anomaly_detection import detect_sales_anomalies
from src.forecasting import forecast_sales
from src.customer_segmentation import segment_customers

# ========== CONFIG ==========
st.set_page_config(
    page_title="SME BI Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)
inject_css()

# ========== DASHBOARD ==========
def dashboard_page(df):
    st.title("SME Business Intelligence Dashboard (Malawi)")
    st.markdown(
        "<span style='font-size:1.1rem;'>Empowering SME owners in Malawi with clear, actionable data.</span>",
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.subheader("Key Performance Indicators")
    render_kpis(calculate_kpis(df))

    st.markdown("---")

    st.subheader("Business Insight")
    st.info(generate_insight(df))

    st.markdown("---")

    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.subheader("Sales by Region")
        fig_region = sales_by_region(df)
        fig_region.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color="#222"),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_region, use_container_width=True)
    with col2:
        st.subheader("Customer Gender Distribution")
        fig_gender = gender_pie(df)
        fig_gender.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(color="#222"),
            margin=dict(l=0, r=0, t=30, b=0)
        )
        st.plotly_chart(fig_gender, use_container_width=True)

    st.markdown("---")

    st.subheader("Customer Age Distribution")
    fig_age = age_distribution(df)
    fig_age.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig_age, use_container_width=True)

# ========== ANOMALY DETECTION ==========
def anomalies_page(df):
    st.title("Real-Time Sales Anomaly Detection")
    st.markdown(
        "<span style='font-size:1.05rem;'>Monitor and detect unusual sales patterns instantly.</span>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    df_anomaly = detect_sales_anomalies(df)
    anomalies = df_anomaly[df_anomaly['Anomaly']]

    if anomalies.empty:
        st.success("No sales anomalies detected.")
    else:
        st.warning(f"{len(anomalies)} sales anomalies detected.")
        st.dataframe(anomalies[['Date', 'Sales']], use_container_width=True)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_anomaly['Date'], y=df_anomaly['Sales'],
        mode='lines', name='Sales', line=dict(color='#064635')
    ))
    if not anomalies.empty:
        fig.add_trace(go.Scatter(
            x=anomalies['Date'], y=anomalies['Sales'],
            mode='markers', name='Anomalies',
            marker=dict(color='red', size=10, symbol='x')
        ))

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)

# ========== FORECASTING ==========
def forecast_page(df):
    st.title("Sales Forecasting")
    st.markdown(
        "<span style='font-size:1.05rem;'>Predict future sales trends to inform business decisions.</span>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    df['Date'] = pd.to_datetime(df['Date'])
    forecast = forecast_sales(df)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=forecast['ds'], y=forecast['yhat'],
        mode='lines', name='Forecast', line=dict(color='#064635')
    ))
    fig.add_trace(go.Scatter(
        x=forecast['ds'], y=forecast['yhat_upper'],
        mode='lines', name='Upper Bound', line=dict(color='#A9D6C1', dash='dash')
    ))
    fig.add_trace(go.Scatter(
        x=forecast['ds'], y=forecast['yhat_lower'],
        mode='lines', name='Lower Bound', line=dict(color='#A9D6C1', dash='dash')
    ))

    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)

# ========== SEGMENTATION ==========
def segmentation_page(df):
    st.title("Customer Segmentation")
    st.markdown(
        "<span style='font-size:1.05rem;'>Identify and visualize customer segments for targeted strategies.</span>",
        unsafe_allow_html=True
    )
    st.markdown("---")

    # Ensure unique customer identifier exists
    if 'Customer ID' not in df.columns:
        df = df.copy()
        df['Customer ID'] = df.index + 1

    df_segmented = segment_customers(df)

    fig = px.scatter(
        df_segmented, x='Customer Age', y='Sales',
        color='Segment',
        color_discrete_sequence=px.colors.sequential.Greens,
        hover_data=['Customer ID']
    )
    fig.update_layout(
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=True)

# ========== FOOTER ==========
def add_footer():
    st.markdown("""
        <hr style="margin-top: 2rem; margin-bottom: 1rem; border: none; border-top: 1px solid #e0e0e0;" />
        <div style="text-align: center; color: #666666; font-size: 0.85rem;">
            SME BI Dashboard · Malawi · Clean. Clear. Data-Driven.
        </div>
    """, unsafe_allow_html=True)

# ========== MAIN ==========
def main():
    st.sidebar.title("SME Dashboard")
    page = st.sidebar.radio("Navigate", [
        "Dashboard",
        "Anomaly Detection",
        "Sales Forecast",
        "Customer Segmentation"
    ])

    df = load_data()
    if df is None or df.empty:
        st.error("No data loaded. Please check your data source.")
        return

    if page == "Dashboard":
        dashboard_page(df)
    elif page == "Anomaly Detection":
        anomalies_page(df)
    elif page == "Sales Forecast":
        forecast_page(df)
    elif page == "Customer Segmentation":
        segmentation_page(df)

    add_footer()

if __name__ == "__main__":
    main()
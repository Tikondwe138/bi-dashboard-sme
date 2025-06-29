import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import io
import xlsxwriter

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

    # Sidebar filters
    regions = df['Region'].unique()
    products = df['Product'].unique()
    date_min, date_max = df['Date'].min(), df['Date'].max()

    selected_regions = st.sidebar.multiselect("Filter by Region", regions, default=list(regions))
    selected_products = st.sidebar.multiselect("Filter by Product", products, default=list(products))
    date_range = st.sidebar.date_input("Date Range", [date_min, date_max])
    if isinstance(date_range, tuple) or isinstance(date_range, list):
        start_date, end_date = date_range[0], date_range[-1]
    else:
        start_date = end_date = date_range

    filtered_df = df[
        (df['Region'].isin(selected_regions)) &
        (df['Product'].isin(selected_products)) &
        (df['Date'] >= pd.to_datetime(start_date)) &
        (df['Date'] <= pd.to_datetime(end_date))
    ]

    # KPIs
    st.subheader("Key Performance Indicators")
    render_kpis(calculate_kpis(filtered_df))
    st.markdown("---")

    # Regional Sales and Gender Distribution side by side
    st.subheader("Regional Sales & Gender Distribution")
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
    st.subheader("Customer Age Distribution")
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
    st.subheader("Business Insight")
    st.info(generate_insight(filtered_df))
    st.markdown("---")

    # Repeat vs. new customers
    filtered_df = filtered_df.sort_values('Date')
    filtered_df['Is New Customer'] = ~filtered_df['Customer ID'].duplicated()
    repeat_count = filtered_df['Is New Customer'].value_counts()
    st.write("New vs. Repeat Customers", repeat_count)

    # Simple churn: customers who haven't purchased in last 30 days
    last_date = filtered_df['Date'].max()
    churned = filtered_df.groupby('Customer ID')['Date'].max() < (last_date - pd.Timedelta(days=30))
    st.write("Churned Customers", churned.sum())

    # Drilldown: click a region bar to see details
    st.subheader("Drilldown: Sales by Region (Filtered)")
    region_fig = sales_by_region(filtered_df)
    region_fig.update_layout(
        autosize=False,
        width=600, height=340,
        margin=dict(l=10, r=10, t=40, b=10),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222")
    )
    st.plotly_chart(region_fig, use_container_width=False)

    # Sales/profit by product
    st.subheader("Sales by Product")
    prod_sales = filtered_df.groupby('Product', as_index=False).agg({'Sales':'sum', 'Profit':'sum'})
    fig_prod = px.bar(prod_sales, x='Product', y='Sales', color='Product', title='Sales by Product')
    fig_prod.update_layout(
        autosize=False,
        width=600, height=340,
        margin=dict(l=10, r=10, t=40, b=10),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222")
    )
    st.plotly_chart(fig_prod, use_container_width=False)

    # Top/bottom products
    top_products = prod_sales.sort_values('Sales', ascending=False).head(3)
    bottom_products = prod_sales.sort_values('Sales').head(3)
    st.write("Top Products", top_products)
    st.write("Bottom Products", bottom_products)

    # Time aggregation option
    agg_option = st.sidebar.selectbox("Aggregate by", ["Daily", "Weekly", "Monthly"])
    if agg_option == "Weekly":
        time_df = filtered_df.resample('W-MON', on='Date').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
    elif agg_option == "Monthly":
        time_df = filtered_df.resample('M', on='Date').agg({'Sales':'sum', 'Profit':'sum'}).reset_index()
    else:
        time_df = filtered_df.copy()

    st.subheader(f"Sales & Profit Over Time ({agg_option})")
    fig_time = px.line(time_df, x='Date', y=['Sales', 'Profit'], title=f'Sales & Profit Over Time ({agg_option})')
    fig_time.update_layout(
        autosize=False,
        width=860, height=320,
        margin=dict(l=10, r=10, t=40, b=10),
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222")
    )
    st.plotly_chart(fig_time, use_container_width=False)

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
        autosize=False,
        width=860, height=320,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=False)

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
        autosize=False,
        width=860, height=320,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=False)

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
        autosize=False,
        width=860, height=320,
        plot_bgcolor='white',
        paper_bgcolor='white',
        font=dict(color="#222"),
        margin=dict(l=0, r=0, t=30, b=0)
    )
    st.plotly_chart(fig, use_container_width=False)

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

    st.sidebar.header("Data Options")
    uploaded_file = st.sidebar.file_uploader("Upload your CSV data", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file, parse_dates=["Date"])
        st.success("Custom data loaded!")
    else:
        df = load_data()

    # Download original/loaded data as CSV
    def convert_df(df):
        return df.to_csv(index=False).encode('utf-8')

    st.sidebar.download_button(
        label="Download Current Data as CSV",
        data=convert_df(df),
        file_name='filtered_data.csv',
        mime='text/csv'
    )

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
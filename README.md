# SME BI Dashboard (Malawi)

A professional, interactive Business Intelligence dashboard for Small and Medium Enterprises (SMEs) in Malawi. Built with Python, Streamlit, and Plotly, this dashboard empowers SME owners and analysts to visualize trends, monitor KPIs, and gain actionable insights from their sales and customer data.

---

## 🚀 Features

- **Data Upload & Download**  
  Upload your own CSV data and download filtered/analyzed data as CSV or Excel.

- **Interactive Filtering**  
  Sidebar filters for Region, Product, and Date Range.

- **Key Performance Indicators**  
  Instant KPIs for sales, profit, and customer metrics.

- **Regional & Demographic Analysis**  
  Visualize sales by region, customer age distribution, and gender breakdown.

- **Product Analysis**  
  Sales and profit by product, with top/bottom product highlights.

- **Time Series Analysis**  
  Line chart for sales/profit over time with daily, weekly, or monthly aggregation.

- **Customer Retention & Churn**  
  See new vs. repeat customers and simple churn analysis.

- **Anomaly Detection**  
  Detect and visualize unusual sales patterns using an Isolation Forest model.

- **Sales Forecasting**  
  Predict future sales trends using Facebook Prophet with upper/lower bounds.

- **Customer Segmentation**  
  Visualize customer segments using K-means clustering.

- **Export Reports**  
  Download filtered data as Excel or CSV.

- **Modern, Responsive UI**  
  Clean, professional UI optimized for desktop and mobile.

---

## 📊 Overview

SMEs in Malawi—whether a shop in Blantyre or a farm input dealer in Lilongwe—often lack access to robust analytical tools. This dashboard solves that with:

- Aggregated sales and customer data
- Automated business insights in plain English
- Interactive visualizations and smart diagnostics
- Low technical overhead with open-source tools

---

## 📂 Project Structure

bi-dashboard-sme/
│
├── data/
│ └── sample_sales_data.csv # Sample dataset
│
├── src/
│ ├── anomaly_detection.py # Isolation Forest logic
│ ├── customer_segmentation.py # K-means clustering
│ ├── data_loader.py # Data import logic
│ ├── forecasting.py # Prophet-based forecasts
│ ├── insights.py # Business rules for summary insights
│ ├── kpis.py # Sales/profit KPI logic
│ ├── localization.py # Currency formatting, translations
│ ├── ui.py # CSS injection, component rendering
│ ├── visuals.py # Plotly visual functions
│ └── generate_sample_data.py # Generates fake sample data
│
├── assets/
│ ├── styles.css # Custom styles
│ └── region_map_malawi.png # (Optional) map asset
│
├── requirements.txt
├── README.md
└── app.py # Streamlit app entry point


---

## 🖥️ Screenshots

> _Add screenshots of your dashboard here to showcase the UI and features._

---

## 🛠️ Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/bi-dashboard-sme.git
    cd bi-dashboard-sme
    ```

2. **Create & activate a virtual environment:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate       # macOS/Linux
    .venv\Scripts\activate          # Windows
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **(Optional) Generate sample data:**
    ```bash
    python src/generate_sample_data.py
    ```

5. **Run the dashboard:**
    ```bash
    streamlit run app.py
    ```

---

## 📈 Usage

- **Dashboard:** View KPIs, charts, and automatic business insights.
- **Anomaly Detection:** Monitor unusual activity in daily sales.
- **Sales Forecast:** View sales predictions for the next 30 days.
- **Customer Segmentation:** Discover distinct customer groups.
- **Data Export:** Download reports and filtered views in CSV/Excel.

> Just drop your own `sample_sales_data.csv` into the `data/` folder and refresh the app.

---

## 🤝 Contribution

Contributions are welcome!

1. Fork the repo
2. Create a branch (`git checkout -b feature-thing`)
3. Commit changes (`git commit -m "Added something cool"`)
4. Push (`git push origin feature-thing`)
5. Open a Pull Request

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

## 📬 Contact

For collaboration, feedback, or questions:  
📧 **mathiusmelo@gmail.com**

---

_This dashboard is here to help SMEs in Malawi turn data into decisions that grow businesses sustainably._



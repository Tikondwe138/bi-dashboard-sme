# BI-Dashboard-SME

Business Intelligence Dashboard for Small and Medium Enterprises (SMEs) in Malawi

---

## Overview

BI-Dashboard-SME is a modular, multi-page analytical tool designed to help Malawian SMEs transform raw sales and customer data into actionable insights. Built with Python, Streamlit and Plotly, it includes:

* **Core Dashboard**: Key performance indicators, regional sales, customer demographics and automated business diagnostics.
* **Real-Time Anomaly Detection**: Machine-learning-driven alerts for unusual sales patterns.
* **Sales Forecasting**: Time-series projections with upper and lower confidence bounds.
* **Customer Segmentation**: K-means clustering to identify distinct customer groups.

By combining data visualization, statistical models and simple machine learning, this application enables SME owners to monitor performance, anticipate demand and tailor marketing strategies with minimal technical overhead.

---

## Case Study and Concept

An SME in Malawi—whether a small retailer in Blantyre or an agro-input supplier in Lilongwe—often lacks the tools to analyze monthly sales trends, detect sudden drops in demand or segment customers by purchasing behavior. BI-Dashboard-SME addresses these challenges by:

1. **Aggregating Sales Data**: imports historical and ongoing transactional data in CSV format.
2. **Computing KPIs**: calculates total sales, profit and profit margin at a glance.
3. **Visualizing Trends**: interactive charts highlight regional performance and customer age/gender breakdowns.
4. **Automated Diagnostics**: natural-language summaries point out the best- and worst-performing regions and margin concerns.
5. **Anomaly Detection**: flags days where sales deviate significantly from expected behavior using an Isolation Forest model.
6. **Forecasting**: extends existing sales patterns into the future using Facebook’s Prophet library.
7. **Segmentation**: applies K-means clustering to group customers for targeted promotions.

This end-to-end workflow—from raw data to strategic recommendations—illustrates how SMEs can use open-source tools to make data-driven decisions without expensive BI licenses or specialized staff.

---

## Features

1. **Core Dashboard**

   * Monthly, quarterly and yearly sales summaries
   * Top-selling products and regional breakdowns
   * Customer age distribution and gender split
   * Automated business insights (in plain English)

2. **Anomaly Detection**

   * Real-time flagging of unusual sales figures
   * Tabular and graphical presentation of anomalies

3. **Sales Forecasting**

   * Future sales projections with confidence intervals
   * Line charts for forecast, upper and lower bounds

4. **Customer Segmentation**

   * Clustering by age and purchase amount
   * Scatter plot of customer segments for easy interpretation

5. **User Interface**

   * Responsive layout for desktop and mobile
   * White-background, black-text theme for maximum readability
   * Sidebar navigation between pages
   * Custom CSS styling for a professional look

---

## Architecture and Folder Structure

```
bi-dashboard-sme/
│
├── data/
│   └── sample_sales_data.csv           # Sample input dataset
│
├── src/
│   ├── anomaly_detection.py            # Isolation Forest model
│   ├── customer_segmentation.py        # K-means clustering
│   ├── data_loader.py                  # CSV import and parsing
│   ├── forecasting.py                  # Prophet forecasting
│   ├── insights.py                     # Business diagnostics
│   ├── kpis.py                         # KPI calculations
│   ├── localization.py                 # Currency formatting and translations
│   ├── ui.py                           # CSS injection and KPI rendering
│   ├── visuals.py                      # Plotly chart functions
│   └── generate_sample_data.py         # Script to create sample CSV
│
├── assets/
│   ├── styles.css                      # Custom CSS for Streamlit
│   └── region_map_malawi.png           # (Optional) map image for future use
│
├── requirements.txt
├── README.md
└── app.py                              # Main entry point with sidebar navigation
```

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/bi-dashboard-sme.git
   cd bi-dashboard-sme
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate       # macOS / Linux
   .venv\Scripts\activate          # Windows
   ```

3. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Generate sample data** (optional)

   ```bash
   python src/generate_sample_data.py
   ```

5. **Run the application**

   ```bash
   streamlit run app.py
   ```

---

## Usage

* **Dashboard**: View KPIs, charts and automated insights.
* **Anomaly Detection**: Monitor daily sales for outliers.
* **Sales Forecast**: See projections for the next 30 days.
* **Customer Segmentation**: Analyze customer clusters to inform marketing.

Use the sidebar to switch between pages. Upload your own `sample_sales_data.csv` in the `data/` folder (same format) and refresh.

---

## Contribution

Contributions, issue reports and feature requests are welcome. To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature-name`)
3. Commit your changes (`git commit -m "Add feature"`)
4. Push to your fork (`git push origin feature-name`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License.

---

## Contact

For questions or collaboration, contact [mathiusmelo@gmail.com](mailto:mathiusmelo@gmail.com).

---

*This dashboard is intended to help Malawian SMEs harness their data to improve decision-making, optimize operations and drive sustainable growth.*

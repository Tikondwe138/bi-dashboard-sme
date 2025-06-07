# src/localization.py

translations = {
    "en": {
        "currency_format": lambda value: f"MWK {value:,.0f}",
        "total_sales": "Total Sales",
        "total_profit": "Total Profit",
        "profit_margin": "Profit Margin",
        "insight_title": "Business Diagnosis",
        "region_sales": "Sales by Region",
        "customer_age": "Customer Age Distribution",
        "gender_split": "Customer Gender Split"
    },
    "ny": {
        "currency_format": lambda value: f"MK {value:,.0f}",
        "total_sales": "Malonda Yonse",
        "total_profit": "Phindu Lonse",
        "profit_margin": "Mphamvu ya Phindu",
        "insight_title": "Kuyerekezera kwa Bizinesi",
        "region_sales": "Malonda Madera",
        "customer_age": "Gawanyo la Msinkhu wa Makasitomala",
        "gender_split": "Gawanyo la Amuna ndi Akazi"
    }
}

current_language = "en"

def t(key):
    return translations[current_language].get(key, key)

def format_currency(value):
    return translations[current_language]["currency_format"](value)

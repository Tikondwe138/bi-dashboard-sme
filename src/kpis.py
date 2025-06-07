def calculate_kpis(df):
    total_sales = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    profit_margin = (total_profit / total_sales * 100) if total_sales > 0 else 0
    return {
        "Total Sales": total_sales,
        "Total Profit": total_profit,
        "Profit Margin (%)": profit_margin,
    }

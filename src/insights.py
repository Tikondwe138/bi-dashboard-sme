from src.localization import format_currency


def generate_insight(df):
    """Generate a simple business insight based on regional sales."""
    if df.empty or "Region" not in df.columns or "Sales" not in df.columns:
        return "Insufficient data to generate insights."

    region_sales = df.groupby("Region")["Sales"].sum().sort_values(ascending=False)
    top_region = region_sales.idxmax()
    drop_region = region_sales.idxmin()
    diff = region_sales.max() - region_sales.min()

    return (
        f"Your best-performing region is {top_region}, "
        f"while {drop_region} had the lowest sales. "
        f"The sales gap between them is {format_currency(diff)}."
    )

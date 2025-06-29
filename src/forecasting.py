import pandas as pd
from prophet import Prophet

def forecast_sales(df, periods=30):
    """
    Forecast future sales using Prophet.

    Args:
        df (pd.DataFrame): DataFrame with columns 'Date' (datetime) and 'Sales' (numeric).
        periods (int): Number of future periods (days) to forecast.

    Returns:
        pd.DataFrame: Forecast dataframe with columns 'ds', 'yhat', 'yhat_lower', 'yhat_upper'.
    """
    # Ensure 'Date' is datetime
    df_prophet = df[['Date', 'Sales']].copy()
    df_prophet['Date'] = pd.to_datetime(df_prophet['Date'])
    df_prophet = df_prophet.rename(columns={'Date': 'ds', 'Sales': 'y'})

    model = Prophet(yearly_seasonality=True, weekly_seasonality=False, daily_seasonality=False)
    model.fit(df_prophet)
    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)
    return forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

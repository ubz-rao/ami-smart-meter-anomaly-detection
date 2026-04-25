import pandas as pd


def create_features(df):
    """
    Creates time-series + behavioral features
    used in AMI anomaly detection.
    """

    df = df.copy()

    # time features
    df["hour"] = df["timestamp"].dt.hour
    df["day_of_week"] = df["timestamp"].dt.dayofweek

    # rolling baseline
    df["rolling_mean"] = df["consumption"].rolling(24).mean()
    df["rolling_std"] = df["consumption"].rolling(24).std()

    # lag feature
    df["lag_1"] = df["consumption"].shift(1)

    # handle missing values
    df = df.bfill()

    return df
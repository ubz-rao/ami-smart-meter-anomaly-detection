from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    """
    Applies Isolation Forest to detect abnormal patterns.
    """

    features = [
        "consumption",
        "hour",
        "day_of_week",
        "rolling_mean",
        "rolling_std",
        "lag_1"
    ]

    model = IsolationForest(
        n_estimators=300,
        contamination=0.05,
        random_state=42
    )

    df["anomaly_score"] = model.fit_predict(df[features])
    df["anomaly_flag"] = (df["anomaly_score"] == -1).astype(int)

    return df
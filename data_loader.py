import numpy as np
import pandas as pd


def load_data(csv_path=None, n_points=1000):
    """
    Loads real AMI consumption data if CSV is provided,
    otherwise generates synthetic smart meter data.
    """

    # REAL DATA MODE (CSV)
    if csv_path:
        df = pd.read_csv(csv_path)

        df.columns = [c.lower().strip() for c in df.columns]

        # detect columns
        time_col = [c for c in df.columns if "time" in c][0]
        cons_col = [c for c in df.columns if "consum" in c or "kwh" in c][0]

        df = df[[time_col, cons_col]]
        df.columns = ["timestamp", "consumption"]

        df["timestamp"] = pd.to_datetime(df["timestamp"])

        return df

    # SIMULATION MODE
    np.random.seed(42)

    timestamp = pd.date_range(
        start="2024-01-01",
        periods=n_points,
        freq="h"
    )

    base = 2 + 0.8 * np.sin(2 * np.pi * timestamp.hour / 24)
    noise = np.random.normal(0, 0.25, n_points)

    consumption = base + noise
    consumption = np.array(consumption)

    # anomalies insertion
    idx = np.random.choice(n_points, int(n_points * 0.05), replace=False)
    consumption[idx] *= np.random.choice([0.2, 3], len(idx))

    return pd.DataFrame({
        "timestamp": timestamp,
        "consumption": consumption
    })
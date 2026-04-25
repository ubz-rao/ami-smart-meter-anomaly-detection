import matplotlib.pyplot as plt


def plot_results(df):
    """
    Visualizes consumption + detected anomalies.
    """

    plt.figure(figsize=(14,6))

    plt.plot(df["timestamp"], df["consumption"], label="Consumption")

    anomalies = df[df["anomaly_flag"] == 1]

    plt.scatter(
        anomalies["timestamp"],
        anomalies["consumption"],
        color="red",
        label="Anomalies"
    )

    plt.title("AMI Smart Meter Anomaly Detection")
    plt.xlabel("Time")
    plt.ylabel("kWh")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
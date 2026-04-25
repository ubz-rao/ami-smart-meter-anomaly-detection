from data_loader import load_data
from feature_engineering import create_features
from model import detect_anomalies
from visualization import plot_results


def main(csv_path=None):

    # Step 1: Load data
    df = load_data(csv_path)

    # Step 2: Feature engineering
    df = create_features(df)

    # Step 3: ML anomaly detection
    df = detect_anomalies(df)

    # Step 4: Summary
    print("\n========================")
    print("AMI ANOMALY REPORT")
    print("========================")
    print(f"Total records: {len(df)}")
    print(f"Anomalies detected: {df['anomaly_flag'].sum()}")

    # Step 5: Visualization
    plot_results(df)


if __name__ == "__main__":

    # For real CSV:
    # main("meter_data.csv")

    # For simulation:
    main()
    
    
    
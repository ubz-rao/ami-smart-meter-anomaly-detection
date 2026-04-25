# Smart Meter Anomaly Detection (AMI Analytics Project)

## Overview

This project demonstrates an anomaly detection system for Smart Meter data used in Advanced Metering Infrastructure (AMI) environments.

The goal is to identify unusual electricity consumption patterns that may indicate:
- Energy theft or non-technical losses
- Meter malfunction
- Abnormal load behavior
- Data inconsistencies in smart grid systems

---

## Industry Context

In AMI systems, utilities collect high-frequency energy consumption data from smart meters. This data is used for monitoring grid health, detecting losses, and ensuring system reliability.

This project simulates a simplified version of an AMI analytics pipeline similar to those used in utility data platforms and meter data management systems.

---

## Approach

The system uses unsupervised machine learning since labeled anomaly data is typically not available in real-world utility datasets.

Model used:
- Isolation Forest (scikit-learn)

This model works by isolating rare patterns in high-dimensional data and is commonly used for anomaly detection problems.

---

## Pipeline

1. Data loading (synthetic or CSV-based smart meter data)
2. Feature engineering (time-based and statistical features)
3. Model training using Isolation Forest
4. Anomaly detection scoring
5. Visualization of results

---

## Features Used

- Electricity consumption (kWh)
- Hour of day
- Day of week
- Rolling mean (24-hour window)
- Rolling standard deviation

---

## Project Structure

This repository contains a modular implementation of an AMI-based smart meter anomaly detection system.

```text
ami-smart-meter-anomaly-detection/
│
├── main.py                      # Entry point of the project
├── data_loader.py              # Data ingestion and loading utilities
├── feature_engineering.py      # Feature creation from raw meter data
├── model.py                    # Isolation Forest model training and prediction
├── visualization.py            # Plotting and result visualization
├── requirements.txt            # Dependencies
└── README.md                   # Project documentation

---

## How to Run

Install dependencies:

pip install -r requirements.txt

Run the project:

python main.py

---

## Output

- Time-series consumption visualization
- Detected anomalies highlighted on the graph
- Summary of anomaly count

---

## Future Enhancements

- Real-time streaming integration (Kafka or MQTT simulation)
- REST API deployment using FastAPI
- Dashboard for monitoring anomalies
- Integration with weather and tariff data
- Advanced deep learning models for temporal patterns

---

## Author

U. B. Zaheer  
AMI Systems Lead | Data and AI Enthusiast
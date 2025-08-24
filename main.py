from src.preprocess import load_logs
from src.model import detect_anomalies
import pandas as pd

def main():
    # טען את הלוגים
    df = load_logs("data/sample_logs.csv")
    if df is None:
        return

    # תכונות שנשתמש בהן
    features = ['event_code', 'hour', 'day_of_week', 'is_weekend']

    # הרצת המודל
    df = detect_anomalies(df, features, contamination=0.1)

    # שמירת התוצאה
    df.to_csv("data/output_with_anomalies.csv", index=False)
    print("Anomaly detection completed. Output saved to data/output_with_anomalies.csv")

if __name__ == "__main__":
    main()

# AI Log Anomaly Detector

This project demonstrates how to use machine learning to detect anomalies in system log files. It is intended for educational purposes in the field of cybersecurity and AI.

## 📌 Features
- Detects unusual events in log files using AI
- Based on IsolationForest algorithm
- Easy to run and customize via Jupyter Notebook
- Sample log files and data included

## 🗂️ Project Structure
```
data/         --> Sample log files (CSV)
notebooks/    --> Jupyter notebooks with ML code
src/          --> Python modules (coming soon)
```

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/pako0174/ai-log-anomaly-detector.git
cd ai-log-anomaly-detector
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the notebook
Navigate to `notebooks/anomaly_detector.ipynb` and run all cells.

## 🧪 Sample Output
The model will label log events as either normal (1) or anomalous (-1). Example output:
```
  event_code  anomaly
0         999       -1
1         503       -1
2         404        1
```

## 📄 License
MIT

---

*Author: Mikel Angel*

# AI Log Anomaly Detector

![Python](https://img.shields.io/badge/python-3.8+-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Last Update](https://img.shields.io/github/last-commit/pako0174/ai-log-anomaly-detector)

This project demonstrates how to use machine learning to detect anomalies in system log files. It is intended for educational purposes in the field of cybersecurity and AI.

## 📌 Features
- Detects unusual events in log files using AI
- Based on IsolationForest algorithm
- Uses time-based features to improve accuracy
- Works in both Jupyter Notebook and CLI mode

## 🗂️ Project Structure
```
data/         --> Sample log files (CSV)
notebooks/    --> Jupyter notebooks with ML code
src/          --> Python modules (preprocessing & model)
main.py       --> CLI script for full pipeline
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
Open `notebooks/anomaly_detector_v2.ipynb` and run all cells.

### 4. Or run from CLI
```bash
python main.py
```

## 📄 License
This project is licensed under the MIT License.

---

*Author: Mikel Angel*

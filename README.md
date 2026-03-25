# Log Monitoring and Anomaly Detection System

## Overview
This project is an end-to-end log monitoring system that performs log generation, parsing, processing, anomaly detection, and visualization using an interactive dashboard.

The system helps identify abnormal system behavior such as errors and critical failures and provides insights through data visualization.

---

## Objectives
- Build a log ingestion pipeline  
- Process and structure log data  
- Detect anomalies based on log severity  
- Visualize logs using a dashboard  
- Provide filtering and monitoring capabilities  

---

## System Architecture

Log Generator → Parser → Processor → Anomaly Detection → Dashboard

---

## Project Structure

log-monitoring-system/
│
├── milestone-1/
├── milestone-2-3-4/
│     ├── pipeline/
│     ├── detection/
│     └── dashboard.py
│
├── milestone-4-documentation/
│     └── Log_Monitoring_End_to_End_Document.pdf
│
├── data/
├── venv/
└── README.md

---

## Technologies Used

- Python  
- Streamlit  
- Pandas  
- Matplotlib  
- Git & GitHub  

---

## Features

- Real-time log generation  
- Log parsing and processing  
- Anomaly detection (ERROR & CRITICAL)  
- Interactive dashboard  
- Filtering by service and log level  
- Metrics and alerts  
- Data visualization using charts  

---

## Dashboard Features

- Total logs, errors, and critical metrics  
- System health alert  
- Service-wise log analysis  
- Log level distribution chart  
- Highlighted anomaly logs  
- Filtering options  

---

## How to Run the Project

1. Clone the repository  
git clone <your-repo-link>

2. Navigate to project folder  
cd log-monitoring-system

3. Activate virtual environment  
venv\Scripts\activate

4. Install dependencies  
pip install -r requirements.txt

5. Run the dashboard  
streamlit run milestone-2-3-4/dashboard.py

---

## Documentation

The complete project documentation is available in:

milestone-4-documentation/

---

## Future Enhancements

- Integration with ELK Stack  
- Real-time streaming using Kafka  
- Machine learning-based anomaly detection  
- Email or notification system  
- Cloud deployment  

---

## Conclusion

This project demonstrates a complete log monitoring system that integrates data processing, anomaly detection, and visualization. It can be extended into a real-world monitoring solution for large-scale systems.
# Log Monitoring System Architecture

## Overview
This system collects logs from applications and detects anomalies automatically.

## Components

### 1. Applications
Applications generate logs such as errors, warnings, and info messages.

### 2. Log Collector
Collects logs from multiple applications and forwards them to storage.

### 3. Log Storage
Stores logs in a centralized system for analysis.

### 4. Anomaly Detection Engine
Analyzes logs using predefined rules from anomaly_schema.yaml to detect unusual behavior.

### 5. Alert System
Sends alerts to administrators when anomalies are detected.

## Data Flow
Applications → Log Collector → Log Storage → Anomaly Detection Engine → Alert System
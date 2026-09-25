# SIEM Integration Engine

A small defensive event-ingestion service that normalizes JSON security events into SQLite.

## Run
```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```
Use POST /ingest and GET /events. Keep integrations restricted to systems you are authorized to monitor.
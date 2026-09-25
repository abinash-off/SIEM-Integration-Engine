# SIEM Integration Engine

Defensive JSON security-event ingestion service with SQLite storage.

## Run
```bash
python -m venv .venv
pip install -r requirements.txt
python app.py
```
POST events to /ingest and inspect them with GET /events. Use only with systems you are authorized to monitor.
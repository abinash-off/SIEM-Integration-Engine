from flask import Flask,request,jsonify
from datetime import datetime,timezone
import sqlite3
app=Flask(__name__); DB="events.db"
def init():
 c=sqlite3.connect(DB); c.execute("CREATE TABLE IF NOT EXISTS events(id INTEGER PRIMARY KEY,source TEXT,event_type TEXT,message TEXT,timestamp TEXT)"); c.commit(); c.close()
@app.post("/ingest")
def ingest():
 d=request.get_json(silent=True) or {}; 
 if not d.get("source") or not d.get("event_type"): return jsonify(error="source and event_type required"),400
 c=sqlite3.connect(DB); c.execute("INSERT INTO events(source,event_type,message,timestamp) VALUES(?,?,?,?)",(str(d["source"])[:100],str(d["event_type"])[:100],str(d.get("message",""))[:1000],d.get("timestamp") or datetime.now(timezone.utc).isoformat())); c.commit(); eid=c.execute("SELECT last_insert_rowid()").fetchone()[0]; c.close(); return jsonify(id=eid),201
@app.get("/events")
def events():
 c=sqlite3.connect(DB); c.row_factory=sqlite3.Row; rows=c.execute("SELECT * FROM events ORDER BY id DESC LIMIT 100").fetchall(); c.close(); return jsonify([dict(r) for r in rows])
@app.get("/health")
def health(): return {"status":"ok"}
if __name__=="__main__": init(); app.run(debug=True)
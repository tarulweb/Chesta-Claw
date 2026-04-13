import sqlite3
import json
from datetime import datetime
from typing import List, Dict, Any
import faiss
import numpy as np

class MemorySystem:
    def __init__(self, db_path: str = "chesta/memory/episodic.sqlite"):
        self.db_path = db_path
        self._init_db()
        self.index = faiss.IndexFlatL2(1536) # Default embedding size

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS episodic (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp DATETIME,
                    goal TEXT,
                    steps TEXT,
                    outcome TEXT,
                    feedback TEXT
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user_model (
                    key TEXT PRIMARY KEY,
                    value TEXT
                )
            """)

    def add_episode(self, goal: str, steps: List[str], outcome: str):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO episodic (timestamp, goal, steps, outcome) VALUES (?, ?, ?, ?)",
                (datetime.now().isoformat(), goal, json.dumps(steps), outcome)
            )

    def update_user_preference(self, key: str, value: Any):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT OR REPLACE INTO user_model (key, value) VALUES (?, ?)",
                (key, json.dumps(value))
            )

    def get_user_preference(self, key: str):
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute("SELECT value FROM user_model WHERE key = ?", (key,)).fetchone()
            return json.loads(row[0]) if row else None

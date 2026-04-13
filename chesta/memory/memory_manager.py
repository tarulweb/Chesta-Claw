import sqlite3
import json
import os
from datetime import datetime
from typing import List, Dict, Any, Optional
import faiss
import numpy as np

class MemorySystem:
    def __init__(self, base_path: str = "chesta/memory"):
        self.db_path = os.path.join(base_path, "episodic.sqlite")
        self.index_path = os.path.join(base_path, "vector.index")
        self.metadata_path = os.path.join(base_path, "metadata.json")

        os.makedirs(base_path, exist_ok=True)
        self._init_db()
        self._init_vector_db()

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

    def _init_vector_db(self):
        # We use a 1536-dim index for OpenAI/OpenRouter embeddings
        if os.path.exists(self.index_path):
            self.index = faiss.read_index(self.index_path)
            with open(self.metadata_path, "r") as f:
                self.metadata = json.load(f)
        else:
            self.index = faiss.IndexFlatL2(1536)
            self.metadata = []

    def add_episode(self, goal: str, steps: List[str], outcome: str, embedding: Optional[np.ndarray] = None):
        # Add to SQLite
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(
                "INSERT INTO episodic (timestamp, goal, steps, outcome) VALUES (?, ?, ?, ?)",
                (datetime.now().isoformat(), goal, json.dumps(steps), outcome)
            )

        # Add to Vector DB if embedding is provided
        if embedding is not None:
            self.index.add(embedding.astype('float32'))
            self.metadata.append({"goal": goal, "timestamp": datetime.now().isoformat()})
            faiss.write_index(self.index, self.index_path)
            with open(self.metadata_path, "w") as f:
                json.dump(self.metadata, f)

    def search_similar_tasks(self, embedding: np.ndarray, top_k: int = 5):
        if self.index.ntotal == 0:
            return []
        D, I = self.index.search(embedding.astype('float32'), top_k)
        results = []
        for idx in I[0]:
            if idx != -1 and idx < len(self.metadata):
                results.append(self.metadata[idx])
        return results

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

"""
Memory-Engine-Py: Embedded DuckDB Memory Layer for Autonomous Agents
Author: Kush Aggarwal (@kushaggarwal2007-byte)
"""
import duckdb
import datetime
from typing import List, Dict, Any

class AgentMemory:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = duckdb.connect(db_path)
        self._init_db()

    def _init_db(self):
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS episodic_memories (
                id VARCHAR PRIMARY KEY,
                category VARCHAR,
                content TEXT,
                created_at TIMESTAMP
            )
        """)

    def record(self, category: str, content: str) -> str:
        mem_id = f"mem_{datetime.datetime.utcnow().timestamp()}"
        self.conn.execute(
            "INSERT INTO episodic_memories VALUES (?, ?, ?, ?)",
            [mem_id, category, content, datetime.datetime.utcnow()]
        )
        return mem_id

    def search(self, query: str) -> List[Dict[str, Any]]:
        cursor = self.conn.execute(
            "SELECT id, category, content, created_at FROM episodic_memories WHERE content ILIKE ? ORDER BY created_at DESC LIMIT 10",
            [f"%{query}%"]
        )
        cols = ["id", "category", "content", "created_at"]
        return [dict(zip(cols, row)) for row in cursor.fetchall()]

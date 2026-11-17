# 🧠 Memory-Engine-Py

> **Production-grade episodic & long-term memory engine for AI agents using embedded DuckDB. Zero cloud DB setup, sub-millisecond local queries.**

[![GitHub stars](https://img.shields.io/github/stars/kushaggarwal2007-byte/memory-engine-py?style=for-the-badge&color=ffd700)](https://github.com/kushaggarwal2007-byte/memory-engine-py/stargazers)
[![License: MIT](https://img.shields.io/badge/License-MIT-blueviolet.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![LinkedIn](https://img.shields.io/badge/Connect-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kush-aggarwal-52a624450)
[![Instagram](https://img.shields.io/badge/Follow-Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white)](https://instagram.com/kushsup)

---

## 💡 Why Memory-Engine-Py?

Most LLM agent memory solutions require bulky cloud vector databases (Pinecone, Weaviate) or bloated Docker stacks.

**Memory-Engine-Py** provides:
- 💾 **Embedded DuckDB Storage**: Run high-performance relational & vector memory on single-file local stores.
- ⏳ **Episodic Context Windows**: Automatically recall past session lessons without exceeding token context limits.
- ⚡ **Atomic Upserts & Compaction**: Zero corruption across concurrent agent workers.
- 🚀 **Zero Dependencies**: Lightweight and embeddable into any Python framework.

---

## 🚀 Quickstart

```bash
git clone https://github.com/kushaggarwal2007-byte/memory-engine-py.git
cd memory-engine-py
pip install -r requirements.txt
```

```python
from memory_engine import AgentMemory

memory = AgentMemory(db_path="agent_brain.duckdb")

# Store episodic observation
memory.record("user_preference", "User prefers concise reports and dark mode charts.")

# Search memories
results = memory.search("reports")
print("Found memories:", results)
```

---

## 👤 Author
Developed by **Kush Aggarwal** — AI Systems Architect & Founder.
- **LinkedIn:** [Kush Aggarwal](https://www.linkedin.com/in/kush-aggarwal-52a624450)
- **Instagram:** [@kushsup](https://instagram.com/kushsup)
- **GitHub:** [@kushaggarwal2007-byte](https://github.com/kushaggarwal2007-byte)

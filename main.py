# main.py - NEXUS V11 API for Render (24x7) - FIXED
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import os

# FIX: tere file ka naam pro.py hai, isliye pro se import
from pro import NexusEngineV11

app = FastAPI(
    title="NEXUS V11 API",
    description="Abhishek XLR - 100B to 1T on 1GB Phone - 16x Compression",
    version="11.0"
)

# Render free me 512MB deta hai, isliye 400MB limit
engine = NexusEngineV11(phone_ram_mb=400)
engine.register_node("render_master_node")
print("NEXUS V11 API Engine Started on Render")

@app.get("/")
def root():
    return {
        "status": "NEXUS V11 LIVE 🔥",
        "owner": "Abhishek pal",
        "engine": "V11 PRO MIXTURE",
        "features": "mmap Zero-Copy + LRU + 16x 2-bit + Swarm Hash",
        "ram": "400MB (Render Free)",
        "model_capacity": "100B in 2 shards | 1T in 20 shards via API swarm",
        "docs": "/docs",
        "health": "/health"
    }

@app.get("/health")
def health():
    # UptimeRobot isi ko har 5 min ping karega taaki API soye nahi
    return {"status": "awake", "engine": "running", "ram_usage": f"{engine.memory_mgr.current_usage/1024:.1f}KB"}

@app.get("/train/{model_size}")
def train(model_size: str = "100B"):
    """
    model_size: 100B, 1T, 60B
    Example: /train/100B
    """
    result = engine.train_large_model_on_mobile(model_size)
    return JSONResponse(content=result)

@app.get("/shard/{shard_id}")
def get_shard(shard_id: str):
    result = engine.train_large_model_on_mobile("100B")
    # Yahi teri STONE AI call karegi
    return {
        "shard_id": shard_id,
        "routing": result["routing"],
        "compression": result["compression"],
        "status": result["status"]
    }

@app.get("/stats")
def stats():
    return {
        "cache_limit_mb": engine.memory_mgr.limit_bytes / 1024 / 1024,
        "current_usage_mb": engine.memory_mgr.current_usage / 1024 / 1024,
        "swarm_nodes": engine.swarm_nodes,
        "phone_ram_config": f"{engine.phone_ram_mb}MB"
    }

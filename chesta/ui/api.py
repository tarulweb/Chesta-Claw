from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from chesta.core.ceo_brain import CEOBrain
from chesta.core.agent_engine import AgentEngine
from chesta.core.router import MultiModelRouter
from chesta.memory.memory_manager import MemorySystem
from chesta.core.skill_engine import SkillEngine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Shared instances
memory = MemorySystem()
router = MultiModelRouter("chesta/models/router_config.json")
engine = AgentEngine()
skills = SkillEngine()
ceo = CEOBrain(engine, router, memory)

@app.get("/status")
async def get_status():
    return {"status": "running", "agents": 1, "memory_usage": "250MB"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        # Handle real-time updates from UI
        await websocket.send_text(f"Message received: {data}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

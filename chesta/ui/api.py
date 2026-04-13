from fastapi import FastAPI, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import asyncio

from chesta.core.ceo_brain import CEOBrain
from chesta.core.agent_engine import AgentEngine
from chesta.core.router import MultiModelRouter
from chesta.memory.memory_manager import MemorySystem
from chesta.core.skill_engine import SkillEngine

app = FastAPI(title="CHESTA CLAW API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Core
memory = MemorySystem()
router = MultiModelRouter()
engine = AgentEngine()
skills = SkillEngine()
ceo = CEOBrain(engine, router, memory)

class GoalRequest(BaseModel):
    goal: str

@app.get("/status")
async def get_status():
    return {
        "status": "online",
        "agents_active": len(engine.active_tasks),
        "memory_episodes": 10, # Placeholder
        "api_health": "100%"
    }

@app.post("/execute")
async def execute_goal(request: GoalRequest):
    try:
        # Run in background to avoid timeout
        asyncio.create_task(ceo.run_goal(request.goal))
        return {"message": "Goal execution started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history():
    # Fetch from memory
    return []

@app.websocket("/ws/logs")
async def websocket_logs(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            # Send real-time updates (simulated for now)
            await websocket.send_json({"type": "log", "message": "CEO: Monitoring API health..."})
            await asyncio.sleep(5)
    except WebSocketDisconnect:
        pass

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

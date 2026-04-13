import asyncio
from typing import List, Dict, Any
from chesta.core.engine import execute_command

class AgentEngine:
    def __init__(self):
        self.active_tasks = {}

    async def run_task(self, task_id: str, command: str):
        print(f"Agent executing task {task_id}: {command}")
        # In the future, this will use Docker/MicroVMs for sandboxing via the Rust engine
        result = execute_command(command)
        return result

    async def stop_task(self, task_id: str):
        if task_id in self.active_tasks:
            # Logic to kill process
            del self.active_tasks[task_id]

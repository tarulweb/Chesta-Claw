import asyncio
from typing import List, Dict, Any
from chesta.core.engine import execute_command

class AgentEngine:
    def __init__(self):
        self.active_tasks = {}

    async def run_task(self, task_id: str, command: str, skill_name: str = None, **kwargs):
        print(f"Agent executing task {task_id}: {command}")

        # Security check before execution
        from chesta.core.security import SecurityManager
        security = SecurityManager()
        if not security.check_command(command):
            return f"Error: Command '{command}' is blocked by security policy."

        if skill_name:
            from chesta.core.skill_engine import SkillEngine
            skills = SkillEngine()
            skills.load_skills()
            return await skills.execute_skill(skill_name, **kwargs)

        # Fallback to Rust engine execution
        result = execute_command(command)
        return result

    async def stop_task(self, task_id: str):
        if task_id in self.active_tasks:
            # Logic to kill process
            del self.active_tasks[task_id]

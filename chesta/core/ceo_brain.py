import asyncio
import time
import json
import os
from typing import List, Dict, Any, Optional
from chesta.core.router import MultiModelRouter

class CEOBrain:
    def __init__(self, engine, router: MultiModelRouter, memory):
        self.engine = engine
        self.router = router
        self.memory = memory
        self.action_history = []
        self.state = {}

    async def run_goal(self, goal: str):
        """Main entry point for executing a high-level goal."""
        print(f"CEO Brain starting goal: {goal}")

        # 1. Decompose
        tasks = await self.decompose_goal(goal)

        results = []
        for task in tasks:
            print(f"CEO: Assigning task: {task['description']}")
            # 2. Assign to agent/skill
            result = await self.execute_task(task)
            results.append(result)

            # 3. Check for loops or issues
            await self.monitor_system()

        # 4. Generate report
        report = await self.generate_completion_report(goal, results)
        return report

    async def decompose_goal(self, goal: str) -> List[Dict[str, Any]]:
        prompt = f"Decompose the following goal into a list of specific, actionable tasks for an AI agent: {goal}. Return JSON list of {{'description': '...', 'skill': '...'}}"
        response = await self.router.call_model([{"role": "user", "content": prompt}], requirement="complex")
        try:
            return json.loads(response)
        except:
            # Fallback decomposition
            return [{"description": goal, "skill": "default"}]

    async def execute_task(self, task: Dict[str, Any]):
        # Implementation of skill execution via engine
        self.action_history.append(task['description'])
        return await self.engine.run_task(str(time.time()), task['description'])

    async def monitor_system(self):
        if len(self.action_history) > 3 and all(x == self.action_history[-1] for x in self.action_history[-3:]):
            print("CEO INTERVENTION: Loop detected!")
            self.action_history = []
            # Trigger intervention logic

    async def generate_completion_report(self, goal: str, results: List[Any]):
        report = {
            "goal": goal,
            "timestamp": time.time(),
            "status": "completed",
            "summary": f"Completed {len(results)} tasks.",
            "results": results
        }
        self.memory.add_episode(goal, [str(r) for r in results], "Success")
        return report

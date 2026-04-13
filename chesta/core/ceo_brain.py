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

            # 3. Check for loops or issues
            if await self.monitor_system():
                # Intervention: try a different model
                print("CEO: Intervening due to loop detection. Switching model...")
                task['requirement'] = 'complex_coding'

            # 2. Assign to agent/skill
            result = await self.execute_task(task)
            results.append(result)

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

    async def supervise(self):
        """Main loop for the CEO Brain to monitor health and generate reports."""
        while True:
            await self.router.check_all_health()
            await self.generate_daily_summary()
            await asyncio.sleep(30)

    async def monitor_system(self):
        if len(self.action_history) > 3:
            last_3 = self.action_history[-3:]
            if all(x == last_3[0] for x in last_3):
                print("CEO INTERVENTION: Infinite loop detected! Switching strategy...")
                self.action_history = []
                # Strategy: rewrite prompt or switch model
                return True
        return False

    async def generate_daily_summary(self):
        """Generates a daily summary of tasks and performance."""
        # Logic to aggregate today's episodes from memory
        pass

    async def generate_completion_report(self, goal: str, results: List[Any]):
        report = {
            "goal": goal,
            "timestamp": time.time(),
            "status": "completed",
            "summary": f"Completed {len(results)} tasks.",
            "results": results
        }
        self.memory.add_episode(goal, [str(r) for r in results], "Success")

        # Self-improvement: Auto-generate SKILL.md
        await self._auto_generate_skill_md(goal, results)
        return report

    async def _auto_generate_skill_md(self, goal: str, results: List[Any]):
        """Hermes-style self-improvement: Capture what worked."""
        skill_name = goal.lower().replace(" ", "_")[:20]
        skill_path = f"chesta/skills/custom/{skill_name}.md"
        content = f"# SKILL: {goal}\n\n## Description\nGenerated from task: {goal}\n\n## Steps Taken\n"
        for i, res in enumerate(results):
            content += f"{i+1}. {res}\n"

        with open(skill_path, "w") as f:
            f.write(content)
        print(f"CEO: New skill documentation generated at {skill_path}")

import os
import importlib.util
from typing import Dict, Any

class SkillEngine:
    def __init__(self, skills_dir: str = "chesta/skills/prebuilt"):
        self.skills_dir = skills_dir
        self.loaded_skills = {}

    def load_skills(self):
        if not os.path.exists(self.skills_dir):
            return
        for filename in os.listdir(self.skills_dir):
            if filename.endswith(".py"):
                skill_name = filename[:-3]
                self.load_skill(skill_name)

    def load_skill(self, skill_name: str):
        path = os.path.join(self.skills_dir, f"{skill_name}.py")
        spec = importlib.util.spec_from_file_location(skill_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        if hasattr(module, "Skill"):
            self.loaded_skills[skill_name] = module.Skill()

    async def execute_skill(self, skill_name: str, **kwargs):
        if skill_name in self.loaded_skills:
            return await self.loaded_skills[skill_name].run(**kwargs)
        raise ValueError(f"Skill {skill_name} not found.")

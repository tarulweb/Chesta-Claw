import pytest
import asyncio
from chesta.core.ceo_brain import CEOBrain
from chesta.core.agent_engine import AgentEngine
from chesta.core.router import MultiModelRouter
from chesta.memory.memory_manager import MemorySystem
from chesta.core.skill_engine import SkillEngine

@pytest.fixture
def setup_system():
    memory = MemorySystem(":memory:") # Use in-memory for tests if possible, but my impl uses path
    # For simplicity in this test, we use the default paths which will be created
    return memory

def test_memory_system():
    ms = MemorySystem("chesta/memory/test.sqlite")
    ms.update_user_preference("test_key", "test_value")
    assert ms.get_user_preference("test_key") == "test_value"
    import os
    if os.path.exists("chesta/memory/test.sqlite"):
        os.remove("chesta/memory/test.sqlite")

def test_skill_loading():
    se = SkillEngine("chesta/skills/prebuilt")
    se.load_skills()
    assert "file_ops" in se.loaded_skills
    assert "web_search" in se.loaded_skills

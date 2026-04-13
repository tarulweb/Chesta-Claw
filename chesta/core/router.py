import httpx
from typing import List, Dict, Any

class MultiModelRouter:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.providers = {
            "openrouter": "https://openrouter.ai/api/v1",
            "ollama": "http://localhost:11434/api",
        }

    async def route(self, skill_requirement: str) -> str:
        """Determines the best model based on cost, speed, and accuracy."""
        # Routing logic: skill requirement → cost → speed → accuracy
        if skill_requirement == "complex_coding":
            return "anthropic/claude-3-opus"
        elif skill_requirement == "fast_task":
            return "google/gemini-flash-1.5"
        return "openrouter/auto"

    async def call_model(self, model_id: str, messages: List[Dict[str, str]], api_key: str):
        """Dispatches the call to the selected provider."""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.providers['openrouter']}/chat/completions",
                headers={"Authorization": f"Bearer {api_key}"},
                json={
                    "model": model_id,
                    "messages": messages
                },
                timeout=60.0
            )
            return response.json()

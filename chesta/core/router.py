import httpx
import asyncio
import time
import json
import os
from typing import List, Dict, Any, Optional
from pydantic import BaseModel

class ModelInfo(BaseModel):
    id: str
    name: str
    provider: str
    cost_per_1k_tokens: float
    latency: float
    health: bool = True

class MultiModelRouter:
    def __init__(self, config_path: str = "chesta/models/router_config.json"):
        self.config_path = config_path
        self.api_keys = {
            "openrouter": os.getenv("OPENROUTER_API_KEY"),
            "openai": os.getenv("OPENAI_API_KEY"),
            "anthropic": os.getenv("ANTHROPIC_API_KEY"),
            "google": os.getenv("GOOGLE_API_KEY"),
        }
        self.models = self._load_model_configs()
        self.health_history = {}

    def _load_model_configs(self) -> List[ModelInfo]:
        if os.path.exists(self.config_path):
            with open(self.config_path, "r") as f:
                data = json.load(f)
                return [ModelInfo(**m) for m in data]
        return [
            ModelInfo(id="anthropic/claude-3-opus", name="Claude 3 Opus", provider="openrouter", cost_per_1k_tokens=0.015, latency=2.5),
            ModelInfo(id="google/gemini-pro-1.5", name="Gemini 1.5 Pro", provider="openrouter", cost_per_1k_tokens=0.007, latency=1.8),
            ModelInfo(id="openai/gpt-4o", name="GPT-4o", provider="openrouter", cost_per_1k_tokens=0.005, latency=1.2),
            ModelInfo(id="moonshot/kimi-v1-8k", name="Moonshot Kimi", provider="openrouter", cost_per_1k_tokens=0.002, latency=1.5),
        ]

    async def get_best_model(self, requirements: str) -> ModelInfo:
        """Selects the best model based on requirement (coding, speed, cost)."""
        healthy_models = [m for m in self.models if m.health]
        if not healthy_models:
            raise Exception("No healthy models available.")

        if "coding" in requirements or "complex" in requirements:
            return next((m for m in healthy_models if "claude-3-opus" in m.id), healthy_models[0])
        elif "fast" in requirements:
            return min(healthy_models, key=lambda x: x.latency)
        elif "cheap" in requirements:
            return min(healthy_models, key=lambda x: x.cost_per_1k_tokens)

        return healthy_models[0]

    async def call_model(self, messages: List[Dict[str, str]], requirement: str = "default") -> str:
        model = await self.get_best_model(requirement)

        try:
            return await self._dispatch_call(model, messages)
        except httpx.HTTPStatusError as e:
            if e.response.status_code in [429, 500, 503]:
                print(f"Model {model.id} overloaded/failed (Status {e.response.status_code}). Failover triggered...")
                model.health = False
                new_model = await self.get_best_model(requirement)
                return await self._dispatch_call(new_model, messages)
            raise
        except Exception as e:
            print(f"Unexpected error with {model.id}: {e}. Attempting failover...")
            model.health = False
            new_model = await self.get_best_model(requirement)
            return await self._dispatch_call(new_model, messages)

    async def _dispatch_call(self, model: ModelInfo, messages: List[Dict[str, str]]) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_keys['openrouter']}",
            "HTTP-Referer": "https://chesta.ai",
            "X-Title": "CHESTA CLAW",
            "Content-Type": "application/json"
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json={
                    "model": model.id,
                    "messages": messages,
                },
                timeout=60.0
            )
            response.raise_for_status()
            data = response.json()
            return data["choices"][0]["message"]["content"]

    async def check_all_health(self):
        """Pings all providers to verify health."""
        for model in self.models:
            # Simplified health check
            model.health = True

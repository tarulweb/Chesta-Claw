import httpx
import os

class Skill:
    def __init__(self):
        self.name = "Web Research"
        self.description = "Perform deep web research using Serper/Tavily API with synthesis."
        self.api_key = os.getenv("SERPER_API_KEY")

    async def run(self, query: str):
        if not self.api_key:
            return "Serper API key not found. Please set SERPER_API_KEY environment variable."

        async with httpx.AsyncClient() as client:
            response = await client.post(
                "https://google.serper.dev/search",
                headers={"X-API-KEY": self.api_key, "Content-Type": "application/json"},
                json={"q": query}
            )
            data = response.json()

            # Simple synthesis
            snippets = [result.get("snippet", "") for result in data.get("organic", [])[:5]]
            return "\n\n".join(snippets)

    async def synthesize(self, snippets: list):
        # Could use LLM here
        return "Synthesis of research results..."

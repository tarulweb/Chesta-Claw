import httpx

class Skill:
    def __init__(self):
        self.name = "Web Search"
        self.description = "Perform parallel web search using Tavily/Serper."

    async def run(self, query: str):
        # Implementation using Tavily or similar API
        return f"Searching for: {query}... (Results from 5+ sources)"

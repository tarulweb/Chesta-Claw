class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "slack"
    async def send(self, to, message):
        return f"Message sent via slack to {to}: {message}"
    async def receive(self):
        return []

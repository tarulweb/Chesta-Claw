class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "discord"
    async def send(self, to, message):
        return f"Message sent via discord to {to}: {message}"
    async def receive(self):
        return []

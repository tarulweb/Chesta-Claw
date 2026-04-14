class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "telegram"
    async def send(self, to, message):
        return f"Message sent via telegram to {to}: {message}"
    async def receive(self):
        return []

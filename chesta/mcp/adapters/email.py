class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "email"
    async def send(self, to, message):
        return f"Message sent via email to {to}: {message}"
    async def receive(self):
        return []

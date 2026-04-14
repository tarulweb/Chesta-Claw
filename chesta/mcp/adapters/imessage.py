class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "imessage"
    async def send(self, to, message):
        return f"Message sent via imessage to {to}: {message}"
    async def receive(self):
        return []

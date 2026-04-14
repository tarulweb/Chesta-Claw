class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "whatsapp"
    async def send(self, to, message):
        return f"Message sent via whatsapp to {to}: {message}"
    async def receive(self):
        return []

class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "$adapter"

    async def send(self, to, message):
        return f"Message sent via $adapter to {to}: {message}"

    async def receive(self):
        return []

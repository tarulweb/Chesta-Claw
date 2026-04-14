class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "messenger"
    async def send(self, to, message):
        return f"Message sent via messenger to {to}: {message}"
    async def receive(self):
        return []

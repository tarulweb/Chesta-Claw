class Adapter:
    def __init__(self, config):
        self.config = config
        self.name = "sms"
    async def send(self, to, message):
        return f"Message sent via sms to {to}: {message}"
    async def receive(self):
        return []

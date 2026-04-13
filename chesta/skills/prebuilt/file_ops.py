import os

class Skill:
    def __init__(self):
        self.name = "File Manager"
        self.description = "Read, write, delete and list files."

    async def run(self, action: str, path: str, content: str = None):
        if action == "read":
            with open(path, "r") as f:
                return f.read()
        elif action == "write":
            with open(path, "w") as f:
                f.write(content)
                return f"File {path} written."
        elif action == "delete":
            os.remove(path)
            return f"File {path} deleted."
        elif action == "list":
            return os.listdir(path)
        return "Invalid action."

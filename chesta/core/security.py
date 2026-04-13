import json
import os

class SecurityManager:
    def __init__(self, whitelist_path: str = "chesta/core/whitelist.json"):
        self.whitelist_path = whitelist_path
        self.dangerous_commands = ["rm", "sudo", "docker", "pip install", "apt"]
        self.whitelist = self._load_whitelist()

    def _load_whitelist(self):
        if os.path.exists(self.whitelist_path):
            with open(self.whitelist_path, "r") as f:
                return json.load(f)
        return []

    def check_command(self, command: str) -> bool:
        """Returns True if command is safe or whitelisted, False otherwise."""
        is_dangerous = any(cmd in command for cmd in self.dangerous_commands)
        if not is_dangerous:
            return True

        return command in self.whitelist

    def whitelist_command(self, command: str):
        if command not in self.whitelist:
            self.whitelist.append(command)
            with open(self.whitelist_path, "w") as f:
                json.dump(self.whitelist, f)

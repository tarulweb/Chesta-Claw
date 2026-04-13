import os
import subprocess
import shutil

class Skill:
    def __init__(self):
        self.name = "System Ops"
        self.description = "Perform sandboxed system operations: create, read, update, delete files and directories."

    async def run(self, action: str, path: str, content: str = None, target: str = None):
        # Whitelist check would go here in Phase 5
        try:
            if action == "create_file":
                os.makedirs(os.path.dirname(path), exist_ok=True)
                with open(path, "w") as f:
                    f.write(content or "")
                return f"File created: {path}"

            elif action == "read_file":
                with open(path, "r") as f:
                    return f.read()

            elif action == "edit_file":
                # Simple overwrite for now, could be improved with search/replace
                with open(path, "w") as f:
                    f.write(content)
                return f"File edited: {path}"

            elif action == "delete_file":
                os.remove(path)
                return f"File deleted: {path}"

            elif action == "rename":
                os.rename(path, target)
                return f"Renamed {path} to {target}"

            elif action == "list_dir":
                return os.listdir(path)

            return f"Unknown action: {action}"
        except Exception as e:
            return f"Error in System Ops: {str(e)}"

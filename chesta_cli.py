import os
import shutil
import sys
import subprocess

def install():
    print("Installing CHESTA CLAW v1.0...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "."], check=True)
        print("Python dependencies installed.")
        subprocess.run(["maturin", "build", "--release"], check=True)
        print("Rust engine built.")

        print("Building UI dashboard...")
        ui_dir = "chesta/ui/dashboard"
        if os.path.exists(ui_dir):
            subprocess.run(["npm", "install"], cwd=ui_dir, check=True)
            subprocess.run(["npm", "run", "build"], cwd=ui_dir, check=True)

        print("Successfully installed.")
    except Exception as e:
        print(f"Installation failed: {e}")

def uninstall(purge=False):
    print("Uninstalling CHESTA CLAW...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", "chesta"], check=True)
        if purge:
            if os.path.exists("chesta"):
                shutil.rmtree("chesta")
            if os.path.exists("chesta/memory"):
                shutil.rmtree("chesta/memory")
        print("Cleanly uninstalled.")
    except Exception as e:
        print(f"Uninstallation failed: {e}")

def main():
    if len(sys.argv) > 1:
        if sys.argv[1] == "install":
            install()
        elif sys.argv[1] == "uninstall":
            purge = "--purge" in sys.argv
            uninstall(purge)

if __name__ == "__main__":
    main()

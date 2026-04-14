# 🏗️ CHESTA CLAW Installation Guide

## 🐧 Linux / 🍏 macOS
1. **System Dependencies**:
   ```bash
   sudo apt install build-essential libssl-dev pkg-config # Linux
   ```
2. **Setup**:
   ```bash
   python chesta_cli.py install
   ```

## 🪟 Windows
1. **Prerequisites**: Install [Visual Studio C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/).
2. **Setup**:
   ```bash
   python chesta_cli.py install
   ```

## 🐳 Docker (Experimental)
```bash
docker build -t chesta-claw .
docker run -p 3000:3000 -p 8000:8000 chesta-claw
```

## ⚠️ Troubleshooting
- **Rust build error**: Ensure `rustc --version` is at least 1.75.
- **Python ModuleNotFound**: Run `pip install -e .` from the root.
- **Next.js issues**: Delete `node_modules` and run `npm install` inside `chesta/ui/dashboard`.

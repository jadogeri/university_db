# FastAPI Setup Commands for Windows

This guide covers creating a virtual environment (`venv`), activating it, and running a **FastAPI** application on Windows.

## 1. Environment Setup

### Create the Virtual Environment
Open your terminal in your project root directory and run:
```cmd
python -m .venv venv
```

### Activate the Environment
Choose the command that matches your terminal type:

* **Command Prompt (cmd):**
  ```cmd
  .venv\Scripts\activate
  ```
* **PowerShell:**
  ```powershell
  .\.venv\Scripts\activate
  ```
### Git Bash / Bash for Windows
```bash
source venv/Scripts/activate
```

*Once activated, you will see `(venv)` at the beginning of your terminal prompt.*

---

## 2. Install Dependencies

Upgrade package manager (`pip`) and install **FastAPI** along with **Uvicorn** (the ASGI production server):

```cmd
python -m pip install --upgrade pip
pip install fastapi uvicorn
```
or

```cmd
python -m pip install --upgrade pip
pip install -e .
```
---



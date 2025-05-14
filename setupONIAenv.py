# Skip Python version check
#python setupONIAenv.py --ignore-version

import sys
import subprocess
import os
import platform
import socket
import time
from datetime import datetime
import sys
import argparse
from typing import List


# === Configuration ===
REQUIRED_PYTHON_VERSION = "3.11.5"
VENV_PATH = r"C:\ONIAenv"
REQUIREMENTS_FILE = "requirements_3.txt"
CHECK_SCRIPT = "packages_to_check.py"
LOG_FILE = "install_log.txt"

os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

import urllib.request
import shutil

def run_pip(args: List[str], venv_python: str):
    subprocess.run([venv_python, "-m", "pip"] + args, check=True)

def download_and_install_python():
    installer_url = "https://www.python.org/ftp/python/3.11.5/python-3.11.5-amd64.exe"
    installer_path = os.path.join(os.getcwd(), "python-3.11.5-amd64.exe")

    log("[INFO] Descărcare installer Python 3.11.5...")
    with urllib.request.urlopen(installer_url) as response, open(installer_path, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    log("[OK] Installer descărcat.")

    log("[INFO] Instalare Python 3.11.5 în mod silențios...")
    result = subprocess.run([
        installer_path,
        "/quiet", 
        "InstallAllUsers=1", 
        "PrependPath=1", 
        "Include_test=0", 
        "SimpleInstall=1"
    ])

    if result.returncode == 0:
        log("[OK] Python 3.11.5 instalat.")
        log("[INFO] Vă rugăm să închideți și să redeschideți terminalul înainte de a continua.")
        sys.exit(0)
    else:
        log("[FATAL] Instalarea Python a eșuat.")
        sys.exit(1)


# === Logging utility ===
def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {message}"
    print(line)
    # Use UTF-8 to avoid UnicodeEncodeError when writing emojis
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

# === Step 1: Check Python version ===
def check_python_version(ignore_version=False):
    version = platform.python_version()
    if ignore_version:
        log(f"[WARN] Ignorăm verificarea versiunii. Detected: {version}")
        return

    if version != REQUIRED_PYTHON_VERSION:
        log(f"[ERROR] Versiunea Python {REQUIRED_PYTHON_VERSION} este necesară. Detectat: {version}")
        answer = input("❓ Vrei să instalăm automat Python 3.11.5 acum? [y/n]: ").strip().lower()
        if answer == 'y':
            download_and_install_python()
        else:
            log("❌ Instalarea s-a oprit. Te rugăm instalează Python manual.")
            sys.exit(1)
    else:
        log(f"[OK] Python {version} este compatibil.")

# === Step 2: Create virtual environment if it doesn't exist ===
def create_virtualenv():
    if args.clean and os.path.exists(VENV_PATH):
        import shutil
        log("[CLEAN] Removing existing virtual environment...")
        shutil.rmtree(VENV_PATH)

    if not os.path.exists(VENV_PATH):
        log("[INFO] Creating virtual environment...")
        subprocess.check_call([sys.executable, "-m", "venv", VENV_PATH])
        subprocess.run([os.path.join(VENV_PATH, "Scripts", "python.exe"), "-m", "ensurepip", "--upgrade"])
    else:
        log("[OK] Virtual environment already exists.")


# === Helper: Run a command inside the virtual environment ===
def run_in_venv(executable, args):
    full_cmd = [executable] + args
    log(f"Running: {executable} + args {args}")

    # Force environment isolation
    env = os.environ.copy()
    env["PYTHONNOUSERSITE"] = "1"  # Ignore user site-packages
    env["PYTHONPATH"] = ""         # Ignore system python path

    subprocess.check_call(full_cmd, env=env)

# === Step 3: Install required packages ===
def install_requirements():
    python_path = os.path.join(VENV_PATH, "Scripts", "python.exe")
    log("[INFO] Upgrading pip...")
    run_pip(["install", "--upgrade", "pip"], python_path)
    log("[INFO] Installing packages from requirements_3.txt...")
    run_pip(["install", "-r", REQUIREMENTS_FILE], python_path)


# === Step 4: Download all NLTK data ===
def download_nltk():
    python_path = os.path.join(VENV_PATH, "Scripts", "python.exe")
    run_in_venv(python_path, ["-c", "import nltk; nltk.download('all')"])

# === Step 5: Test that all important packages import successfully ===
def test_imports():
    python_path = os.path.join(VENV_PATH, "Scripts", "python.exe")
    log("[TEST] Verifying imports in packages_to_check.py...")
    try:
        run_in_venv(python_path, [CHECK_SCRIPT])
        log("[OK] All packages imported successfully.")
    except subprocess.CalledProcessError:
        log("[ERROR] Import check failed.")
        sys.exit(1)

# === Step 6: Test that Jupyter Lab runs and responds ===
def test_jupyter_lab():
    python_path = os.path.join(VENV_PATH, "Scripts", "python.exe")
    log("[TEST] Starting Jupyter Lab...")
    proc = subprocess.Popen([python_path, "-m", "jupyter", "lab", "--no-browser"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(10)  # Give it time to start

    # Check if default Jupyter port 8888 is open
    log("[TEST] Checking if port 8888 is responding...")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex(("localhost", 8888))
    s.close()

    if result == 0:
        log("[OK] Jupyter Lab is running on port 8888.")
    else:
        log("[ERROR] Jupyter Lab did not start correctly.")
        proc.terminate()
        sys.exit(1)

    # Kill Jupyter Lab after test
    proc.terminate()

def patch_activate_bat():
    activate_path = os.path.join(VENV_PATH, "Scripts", "activate.bat")
    if not os.path.exists(activate_path):
        log("[WARN] activate.bat not found, skipping oneDNN patch.")
        return

    with open(activate_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    already_set = any("TF_ENABLE_ONEDNN_OPTS=0" in line for line in lines)
    if already_set:
        log("[OK] activate.bat already sets TF_ENABLE_ONEDNN_OPTS=0.")
        return

    # Insert just after the header comments (or at top)
    insert_line = "set TF_ENABLE_ONEDNN_OPTS=0\n"
    lines.insert(0, insert_line)

    with open(activate_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    log("[INFO] Patched activate.bat to set TF_ENABLE_ONEDNN_OPTS=0.")

def install_vscode_extensions():
    log("[INFO] Checking for VS Code executable...")

    # Common install locations
    possible_paths = [
        os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft VS Code", "bin", "code.cmd"),
        os.path.join(os.environ.get("ProgramFiles", ""), "Microsoft VS Code", "Code.exe"),
        os.path.join(os.environ.get("LocalAppData", ""), "Programs", "Microsoft VS Code", "bin", "code.cmd"),
        os.path.join(os.environ.get("LocalAppData", ""), "Programs", "Microsoft VS Code", "Code.exe"),
    ]

    code_path = None
    for path in possible_paths:
        if os.path.isfile(path):
            code_path = path
            break

    if code_path is None:
        log("[WARN] VS Code not found. Please install the Jupyter and Python extensions manually.")
        return

    log(f"[OK] Found VS Code at: {code_path}")
    try:
        subprocess.check_call([code_path, "--install-extension", "ms-toolsai.jupyter", "--force"])
        subprocess.check_call([code_path, "--install-extension", "ms-python.python", "--force"])
        log("[OK] VS Code extensions installed successfully.")
    except subprocess.CalledProcessError as e:
        log(f"[ERROR] Failed to install extensions: {e}")

# === Main entry point ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ONIA Environment Setup")
    parser.add_argument("--ignore-version", action="store_true", help="Skip Python version check")
    parser.add_argument("--clean", action="store_true", help="Delete and recreate the virtual environment")
    args = parser.parse_args()


    install_vscode_extensions()

    log("=== ONIA Environment Setup & Verification ===")
    try:
        check_python_version(ignore_version=args.ignore_version)
        create_virtualenv()
        install_requirements()
        download_nltk()
        patch_activate_bat()
        test_imports()
        test_jupyter_lab()
        log("[SUCCESS] ONIA environment setup and verification complete.")
    except Exception as e:
        log(f"[FATAL] Script failed: {e}")
        sys.exit(1)

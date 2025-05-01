import subprocess
import shutil
import sys

def run_command(cmd):
    print(f"\n[Running]: {cmd}")
    try:
        subprocess.run(cmd, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"[Error]: Failed to execute: {cmd}")
        sys.exit(1)

if not shutil.which("wget"):
    print("[Info]: wget not found, installing...")
    run_command("sudo apt update && sudo apt install -y wget")

if not shutil.which("unzip"):
    print("[Info]: unzip not found, installing...")
    run_command("sudo apt update && sudo apt install -y unzip")

commands = [
    "sudo apt update && sudo apt upgrade -y",
    "wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb",
    "sudo dpkg -i google-chrome-stable_current_amd64.deb",
    "sudo apt install -y libxss1 libappindicator3-1 libindicator7 libatk-bridge2.0-0 libatk1.0-0 libcups2 libgdk-pixbuf2.0-0 libnspr4 libnss3 libx11-xcb1 libxcomposite1 libxrandr2 libgdk-pixbuf2.0-0 libpangocairo-1.0-0",
    "wget https://storage.googleapis.com/chrome-for-testing-public/135.0.7049.114/linux64/chromedriver-linux64.zip",
    "unzip chromedriver-linux64.zip",
    "cd chromedriver-linux64 && chmod +x chromedriver && sudo mv chromedriver /usr/local/bin/"
]

for cmd in commands:
    run_command(cmd)

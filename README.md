
# H I J A X

**Session Hijacking Framework by ekomsSavior**
 

Hijax is a tool for hijacking live user sessions via stolen browser tokens, cookies, and OAuth strings.  
It mimics how real attackers hijack Discord, Instagram, Google, and Facebook ETC. accounts without ever logging in.

> **Educational & ethical use only** 

---

##  Features

-  Steal cookies and tokens from Chrome & Firefox
-  Monitor clipboard for leaked tokens (Discord, JWTs, Bearer, etc.)
-  Inject stolen tokens into a live browser session (via Selenium)
-  Replay sessions via HTTP requests (no browser needed)
-  Dump DMs, friend lists, drive files, and profile info
-  Headless + interactive modes

---

##  Project Structure

```
hijax/
├── hijax_cli.py             # CLI with banner and menu
├── token_harvester.py       # Steals browser cookies
├── token_injector.py        # Injects cookies into browser session
├── token_replayer.py        # Hits APIs using stolen cookies
├── utils/
│   ├── clipboard_monitor.py # Passive token logger from clipboard
│   └── browser_parser.py    # (optional future logic)
├── loot/
│   └── stolen_tokens.txt    # All harvested tokens go here
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the repo

```bash
git clone https://github.com/yourname/hijax.git
cd hijax
```

2. Install dependencies

sudo apt update
sudo apt install -y python3 python3-pip chromium-driver
pip3 install -r requirements.txt --break-system-packages


⸻

 Run Hijax

python3 hijax_cli.py


⸻

 Module Breakdown

1. Harvest Cookies

python3 token_harvester.py

	•	Scans Chrome and Firefox for cookies from:
	•	instagram.com
	•	discord.com
	•	google.com
	•	facebook.com
	•	icloud.com
	•	Dumps everything to loot/stolen_tokens.txt
	•	Also logs system fingerprint (IP, hostname)

⸻

 2. Clipboard Monitor

python3 utils/clipboard_monitor.py

	•	Runs in background
	•	Logs any token-like strings you copy to clipboard (JWTs, Discord tokens, Bearer headers)

⸻

 3. Inject Token into Live Browser

python3 token_injector.py

	•	Opens Chromium browser
	•	Injects cookies for:
	•	Instagram
	•	Discord
	•	Facebook
	•	Google
	•	Reloads the site as the hijacked user

⸻

 4. Replay Session via API

python3 token_replayer.py

	•	Headless (no browser)
	•	Uses stolen cookies to:
	•	Dump Discord DMs
	•	Check Google Drive access
	•	View Instagram profile
	•	Access Facebook mobile session

⸻

 DISCLAIMER
	•	Always test with your own accounts and lab data
	•	Never use Hijax on unauthorized targets 

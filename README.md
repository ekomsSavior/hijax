# H I J A X

**Session Hijacking Framework by ekomsSavior**
*“Steal sessions. Own devices. Replay reality”*

---

Hijax is a red team tool designed to hijack live user sessions from browser environments. It mimics how real-world stealers and web-based implants exfiltrate tokens and hijack authenticated sessions across platforms like:

*  Discord
*  Instagram
*  Facebook
*  Google
*  iCloud
*  Anything that stores session cookies

>  **For educational and ethical testing purposes only.** Use only on systems you own or have permission to test.

---

## Features

*  Extract session cookies from Chrome/Firefox
*  Capture clipboard tokens (Discord, JWT, OAuth)
*  Inject cookies directly into browser (bypass login/2FA)
*  Replay sessions via HTTP requests (no GUI needed)
*  Serve implants via ScamTrack (HTML+JS drop)
*  Reuse hijacked sessions for DM dumping, file list extraction, and more

---

## Project Structure

```
hijax/
├── hijax_cli.py             # Menu-based launcher
├── token_harvester.py       # Extracts browser cookies (local)
├── token_injector.py        # Injects session cookies into browser
├── token_replayer.py        # Headless API session impersonation
├── hijax_remote_implant.py  # Implant for remote cookie dumping (via C2 or webhook)
├── utils/
│   ├── clipboard_monitor.py # Clipboard listener (optional)
│   └── browser_parser.py    # (future: Chrome/Firefox master key decryptor)
├── loot/
│   └── stolen_tokens.txt    # Extracted tokens saved here
├── README.md
```

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourname/hijax.git
cd hijax
```

### 2. Install required tools and libraries

```bash
sudo apt update && sudo apt install python3 python3-pip chromium-driver curl jq unzip -y
```

```bash
pip3 install selenium requests browser-cookie3 beautifulsoup4 pycryptodome pyperclip --break-system-packages
```

---

## How to Use

### Launch the CLI

```bash
python3 hijax_cli.py
```

This gives you a clean menu to:

* \[1] Harvest cookies
* \[2] Inject token into browser
* \[3] Replay session headlessly
* \[4] Exit

---

### \[1] Harvest Browser Cookies

```bash
python3 token_harvester.py
```

* Scans Chrome and Firefox for stored session cookies
* Targets sites like Instagram, Discord, Google, Facebook, and iCloud
* Also logs system fingerprint info (hostname, IP, timestamp)
* Saves all output to `loot/stolen_tokens.txt`

---

###  \[2] Clipboard Monitor (Optional)

```bash
python3 utils/clipboard_monitor.py
```

* Monitors your clipboard for stolen tokens (Discord, MFA, JWTs, etc.)
* Auto-writes any matches to `stolen_tokens.txt`
* Great for watching what gets copied during phishing payload use

---

###  \[3] Inject Tokens Into Live Browser Session

```bash
python3 token_injector.py
```

* Opens a Selenium browser
* Lets you choose a target (e.g., Instagram)
* Injects matching cookies from `stolen_tokens.txt`
* Reloads the page — you’re now impersonating the real user 🔓

---

###  \[4] Replay Sessions (Headless API Access)

```bash
python3 token_replayer.py
```

* No browser needed — works with raw tokens
* Lets you impersonate the user via API endpoints:

  * Dump Discord DMs
  * View Instagram profile
  * List Google Drive contents
  * Pull Facebook mobile session

---

##  Implant Delivery Mode

Use **Hijax with ScamTrack or GhostMode** to launch HTML-based session stealers.

### Example: `hijax_browser_implant.html`

* Hosted via Flask + Ngrok
* Extracts:

  * `document.cookie`
  * `localStorage`
  * Clipboard text (if permissions allow)
* Sends to Flask route `/api/hijax`
* Logs to `loot/hijax_loot.txt`
* Silently redirects user (e.g. to instagram.com)

### How to Use:

1. Load it into ScamTrack payload folder
2. Build a trap link or QR code
3. User scans the tag or opens the link
4. Loot is logged + parsed

---

## Remote Mode

### Drop `hijax_remote_implant.py` onto a victim machine

* Steals cookies from Chrome silently
* Logs device info
* Sends `stolen_tokens.txt` back to a Discord webhook or C2
* Works like a miniature info-stealer, no malware dependencies

Use `token_replayer.py` to replay those tokens from attacker box.

---

## Token Sources Hijax Supports

| Target Platform | Method of Hijack                           |
| --------------- | ------------------------------------------ |
| Instagram       | `sessionid`, `ds_user_id` (cookies)        |
| Discord         | `token`, `__dcfduid` (cookie or clipboard) |
| Google          | `SID`, `SAPISID` (browser cookie)          |
| Facebook        | `c_user`, `xs` (browser cookie)            |
| iCloud          | MEAuthToken (if extracted)                 |

---

##  Disclaimer

* Hijax is for red team simulation, education, and security awareness.
* Do not use this tool against live systems without **explicit permission**.
* Hijacking session cookies is illegal without consent and may violate CFAA or other laws.


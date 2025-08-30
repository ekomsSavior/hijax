# H I J A X

**Session Hijacking Framework by ekomsSavior**

*“Steal sessions. Own devices. Replay reality.”*

---

Hijax is a modular red team framework built to demonstrate and simulate **session hijacking** from browsers and infected hosts. It exfiltrates tokens and hijacks authenticated sessions across:

* Discord
* Instagram
* Google
* Facebook
* iCloud
* Any platform that stores session cookies or OAuth tokens

>  **For educational and ethical testing only. Do not use on targets you do not own or have explicit permission to assess.**

---

##  Features

* Extract live session cookies from Chrome/Firefox
* Hijack sessions via browser cookie injection
* Replay sessions via API access (no GUI needed)
* Monitor clipboard for Discord or JWT tokens
* Drop browser or remote implants for passive exfiltration
* Auto-generate a standalone **implant script** to deploy to remote systems
* Seamless integration with [ScamTrack](https://github.com/yourorg/scamtrack) for HTML+JS payload delivery

---

![Screenshot_2025-08-29_10_52_12](https://github.com/user-attachments/assets/1948d982-60c7-4974-8dd4-8da4c43d40d1)

---

##  Installation

### Clone the Repo

```bash
git clone https://github.com/ekomsSavior/hijax.git
cd hijax
```

### Install Dependencies

```bash
sudo apt update && sudo apt install -y python3 python3-pip chromium-driver curl jq unzip
pip3 install selenium requests browser-cookie3 beautifulsoup4 pycryptodome pyperclip --break-system-packages
```

---

##  How to Use

### Launch the CLI

```bash
python3 hijax_cli.py
```

This gives you :

![hijax](https://github.com/user-attachments/assets/c48b119e-c10c-473f-a6b5-995aff1fa6b4)

---

### Cookie Harvester

```bash
python3 token_harvester.py
```

* Extracts session cookies from Chrome/Firefox
* Dumps everything to `loot/stolen_tokens.txt`
* Logs IP, hostname, timestamps, and platform

---

###  Clipboard Token Monitor

```bash
python3 utils/clipboard_monitor.py
```

* Watches 24/7 for Discord, JWT, MFA tokens copied to clipboard
* Writes loot directly to `loot/stolen_tokens.txt`

---

###  Token Injection (Browser Hijack)

```bash
python3 token_injector.py
```

* Launches Chromium with Selenium
* Injects stolen cookies into a live session
* Bypasses login/2FA and impersonates the victim

---

###  Headless API Replay (No GUI)

```bash
python3 token_replayer.py
```

* Allows recon, DM dumping, file listing, etc. via API
* Works with Discord, Instagram, Facebook, Google, and others
* No GUI needed — all token-based impersonation

---

##  Implant Builder (NEW!)

```bash
[4] Generate Implant via CLI
```

* Auto-generates a fully functional Python implant:

  * `hijax_remote_implant.py`
* Can be deployed on remote systems to extract and send tokens back
* Logs Chrome cookies + device fingerprint
* Sends data to your webhook or stores it locally
* No malware dependencies, simple + stealthy

 Use this when:

* You want a creds stealer
* You want to bundle it into another payload
* You want to serve the implant via ScamTrack/QR

---

##  ScamTrack Integration

Hijax was designed to work natively with **ScamTrack** for browser-based payload delivery.

###  Payload: `hijax_browser_implant.html`

* Grabs:

  * `document.cookie`
  * `window.localStorage`
  * Clipboard contents (if available)
* Sends it to:

  ```
  POST /api/hijax
  ```
* Output stored in: `loot/hijax_loot.txt`
* Optional redirect to legit site (e.g., Instagram)

###  How to Deploy via ScamTrack

1. Drop `hijax_browser_implant.html` into the ScamTrack `payloads/` directory
2. Start the Flask server via ScamTrack CLI
3. Ngrok URL will serve the implant
4. Share QR code or phishing link
5. Results get logged + parsed by Hijax


---

##  Token Sources & Methods

| Platform  | Method                    | Source                 |
| --------- | ------------------------- | ---------------------- |
| Discord   | `token`, `__dcfduid`      | Cookie or clipboard    |
| Instagram | `sessionid`, `ds_user_id` | Cookie                 |
| Google    | `SID`, `SAPISID`          | Cookie                 |
| Facebook  | `c_user`, `xs`            | Cookie                 |
| iCloud    | `MEAuthToken`             | Cookie or localStorage |

---

##  Red Team Workflow

1. Harvest or generate implant from Hijax CLI
2. Serve implant via ScamTrack or deploy directly
3. Tokens are exfiltrated to attacker machine
4. Replay session or inject into Selenium browser
5. Dump user data, messages, sessions, etc.

---

##  Disclaimer

Hijax is for **educational**, **research**, and **red team simulation** only.

Do **not** use against real systems, individuals, or networks without **explicit written permission**.
Unauthorized use may violate CFAA, GDPR, or other laws.

![Screenshot_2025-08-29_10_52_12(1)](https://github.com/user-attachments/assets/ebbe32d7-cfe5-4aa7-872c-bc0d2d326d7c)

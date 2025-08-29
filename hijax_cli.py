#!/usr/bin/env python3
import time

BANNER = r'''
  ▄█    █▄     ▄█       ▄█    ▄████████ ▀████    ▐████▀ 
 ███    ███   ███      ███   ███    ███   ███▌   ████▀  
 ███    ███   ███▌     ███   ███    ███    ███  ▐███    
▄███▄▄▄▄███▄▄ ███▌     ███   ███    ███    ▀███▄███▀    
▀▀███▀▀▀▀███▀  ███▌     ███ ▀███████████    ████▀██▄     
  ███    ███   ███      ███   ███    ███   ▐███  ▀███    
  ███    ███   ███      ███   ███    ███  ▄███     ███▄  
  ███    █▀    █▀   █▄ ▄███   ███    █▀  ████       ███▄ 
                    ▀▀▀▀▀▀                                
'''

MENU = '''
[1] Harvest Tokens
[2] Inject Token in Browser
[3] Replay Session (API Mode)
[4] Generate Remote Implant (HTML Payload)
[0] Exit
'''

def main():
    print(BANNER)
    time.sleep(1)
    print("Welcome to H I J A X – Session Hijacking Framework\n")
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            import token_harvester
            token_harvester.run()
        elif choice == "2":
            import token_injector
            token_injector.run()
        elif choice == "3":
            import token_replayer
            token_replayer.run()
        elif choice == "4":
            from hijax_remote_implant import generate_payload
            generate_payload()
        elif choice == "0":
            print("bye bye hacker 💀")
            break
        else:
            print("[!] Invalid option. Try again.")

if __name__ == "__main__":
    main()

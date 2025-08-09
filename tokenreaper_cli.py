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
Session Hijacking Framework by ekomsSavior
'''

MENU = '''
[1] Harvest Tokens
[2] Inject Token in Browser
[3] Replay Session (API Mode)
[4] Exit
'''

def main():
    print(BANNER)
    time.sleep(1)
    print("Welcome to TOKENREAPER – Session Hijacking Framework\n")
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
            print("Goodbye hacker 💀")
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()

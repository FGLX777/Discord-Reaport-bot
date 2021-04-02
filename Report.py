import requests,colorama,os,time
from time import sleep
from colorama import Fore, Style
colorama.init()


def logo():
    msg = Fore.LIGHTRED_EX +"""
    ██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗ ███████╗██████╗  ██████╗ ██████╗ ████████╗
    ██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔════╝██╔══██╗██╔═══██╗██╔══██╗╚══██╔══╝
    ██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝█████╗  ██████╔╝██║   ██║██████╔╝   ██║   
    ██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██╗██╔══╝  ██╔═══╝ ██║   ██║██╔══██╗   ██║   
    ██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██║  ██║███████╗██║     ╚██████╔╝██║  ██║   ██║   
    ╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═╝  ╚═╝╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝   ╚═╝ """
    print(msg)
logo()
print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Would you like to use multiple accounts? [Y / N]: ")
mass = input("")
os.system("cls")
logo()
if mass == "y":
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Token Txt: ")
    txt = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Illegal Content [1]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Harrassment [2]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Spam or Phishing Links [3]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Self harm [4]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"NSFW Content [5]")
    reason = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Message ID: ")
    message = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Channel ID: ")
    Channel = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Guild ID: ")
    Guild = input("")
    os.system("cls")
    logo()
    while True:
        with open(txt) as f:
            token = line.strip("\n")
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
                'Authorization': token,
                'Content-Type': 'application/json'
            }
            payload = {
                'channel_id': Channel,
                'guild_id': Guild,
                'message_id': message,
                'reason': reason
            }
            r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
            ID = r.json()['id']
            print(Fore.LIGHTGREEN_EX+"[ OK ] "+Fore.RESET+f"Report ID[{ID}]")
else:
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Account Token: ")
    token = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Illegal Content [1]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Harrassment [2]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Spam or Phishing Links [3]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"Self harm [4]")
    print(Fore.LIGHTBLUE_EX+"[ * ] "+Fore.RESET+"NSFW Content [5]")
    reason = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Message ID: ")
    message = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Channel ID: ")
    Channel = input("")
    os.system("cls")
    logo()
    print(Fore.LIGHTBLUE_EX+"[ ? ] "+Fore.RESET+"Guild ID: ")
    Guild = input("")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36',
        'Authorization': token,
        'Content-Type': 'application/json'
    }
    os.system("cls")
    logo()
    while True:
        payload = {
            'channel_id': Channel,
            'guild_id': Guild,
            'message_id': message,
            'reason': reason
        }
        r = requests.post('https://discord.com/api/v6/report', headers=headers, json=payload)
        ID = r.json()['id']
        print(Fore.LIGHTGREEN_EX+"[ OK ] "+Fore.RESET+f"Report ID[{ID}]")

    
    
    






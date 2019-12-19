import discord
import asyncio
import sys
from discord.ext import commands
import requests
import os
import json
import threading
import time
from os import system
from subprocess import call 
import ctypes
from time import sleep 
from colorama import Fore,init
import sys
import threading
version= "1.0"

alb = Fore.WHITE
rosu = Fore.RED
verde = Fore.GREEN
init()
clear = lambda: os.system("cls")

version = "1.0"

ui = f'''{Fore.CYAN}

                     _   _                                                                 
                    | | | |                                                                
                    | |_| | __ _ _ __  ___   ___ _ __   __ _ _ __ ___  _ __ ___   ___ _ __ 
                    |  _  |/ _` | '_ \/ __| / __| '_ \ / _` | '_ ` _ \| '_ ` _ \ / _ \ '__|
                    | | | | (_| | | | \__ \ \__ \ |_) | (_| | | | | | | | | | | |  __/ |   
                    \_| |_/\__,_|_| |_|___/ |___/ .__/ \__,_|_| |_| |_|_| |_| |_|\___|_|   
                                                | |                                        
                                                |_|                         Version: {version}               

                                                                                                                        
    '''



def spammer():
    clear()
    ctypes.windll.kernel32.SetConsoleTitleW("Hans spammer | v{}".format(version))
    init()
    print(ui)
    print()

    print(Fore.BLUE+f'[1]{Fore.WHITE} Join server')
    print(Fore.BLUE+f'[2]{Fore.WHITE} Spam server')
    print(Fore.BLUE+f'[3]{Fore.WHITE} Spam friend request')
    print()


    init()
    print(Fore.CYAN + f'Choose an option:{Fore.WHITE} ', end='' + Fore.WHITE)
    option = str(input())


    sent = 0
    joinedt = 0
    num = 0


    token1 = []
    def load_token1():
                with open('tokens.txt', 'r') as f:
                        for x in f.readlines():
                                token1.append(x.replace('\n',''))




    if option =='1':
        link = input(Fore.CYAN+f'Discord Invite Link(link):{Fore.WHITE} ')
        if len(link) > 6:
            link = link[19:]
            apilink = "https://discordapp.com/api/v6/invite/" + str(link)

            print(f"{Fore.CYAN}Adding bots to server:{Fore.WHITE} {link}")
            s = 0
            with open('tokens.txt','r') as handle:
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
        with open('tokens.txt', 'r') as handle:
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

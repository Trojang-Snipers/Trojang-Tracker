import requests
import time
from colorama import *
from art import *

def track(message):
    URL = "https://api.hypixel.net/player?key=046ce573-8b06-40f2-96b2-86fcb834be15&uuid=" + requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()['id']
    print(URL)
    data = requests.get(URL)
    datajson = data.json()
    stat1 = (datajson['player']['stats']['Bedwars']["losses_bedwars"])
    stat3 = (datajson['player']['stats']['Bedwars']["wins_bedwars"])
    wins = int(stat3)
    losses = int(stat1)
    while True:
        time.sleep(1)
        data = requests.get(URL)
        e = data.json()
        loss = (e['player']['stats']['Bedwars']["losses_bedwars"])
        win = (e['player']['stats']['Bedwars']["wins_bedwars"])
        countwin = 1
        countloss = 1
        if win == wins + countwin:
            countwin += 1
            print(requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()['name'] + ' Has Won A Match Of Bedwars')
        if loss == losses + countloss:
            countloss += 1
            print(requests.get(f"https://api.mojang.com/users/profiles/minecraft/{message}").json()['name'] + ' Has Lost A Match Of Bedwars')

init()
print(Fore.MAGENTA + '')
tprint('TroTracker')
print('--------------------- >> By iTrojang#7855 << ---------------------')
while True:
    cmd = input('[TroTracker]Enter Command (/help For List) >> ')
    if cmd == '/help':
        print("---[Command List]--- \n /help - shows this message. \n /track <ign> - Sets a Tracker On a specific ign.")
    if cmd[:7] == '/track ':
        track(cmd[7:])

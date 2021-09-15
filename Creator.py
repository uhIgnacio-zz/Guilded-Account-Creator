import requests
import random
import string
import threading
import os
from threading import Thread
from colorama import Fore, Style, init

#https://www.guilded.gg/api/invites/42DOaQ7E?teamId=Oj1oeMpl&

webhook = "https://media.guilded.gg/webhooks/3f6dc5da-a793-46af-933c-5bb549a42dd5/pIV33KLlg4SWc8CoEw0ISw0ScKc4YAGkUKa66Y6couwoQY6S6SoUaGaquIE0uCQiGwAmi4uiq8aU0YAUSkq44o"

proxies = open('proxies.txt').read().splitlines()

def getProxy():
    return({'https': f'http://{random.choice(proxies)}'})

def create(name, email, password):
    try:
        proxy = getProxy()
        #creator
        requests.post('https://www.guilded.gg/api/users?type=email', headers={'Content-Type': 'application/json','guilded-client-id': '17119702-e1c6-4d8f-8920-4f7ca425b84d', 'guilded-device-id': '537b5c96c662685a3c6a9cf97b15fafe68ca4eb5141254ac908d08f4460218cc', 'guilded-device-type': 'desktop', 'guilded-stag': '0646ede6507f50ace615efb1c9d14b48','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153'}, json = {'name': name, 'email': email, 'password': password, 'fullName': name}, proxies=proxy)
        r2 = requests.post('https://www.guilded.gg/api/login', json = {'email': email, 'password': password, 'getMe': True}, proxies=proxy)
        cookie = str(r2.cookies).split('hmac_signed_session=')[1].split(' ')[0]
        if r2.status_code == 200:
            print(f"> | Succesfully Created New Account: {name}\n")
            #webhook
            requests.post(webhook, json={"content": cookie}, proxies=proxy)
        else:
            print(f"? | Failed to Create Account: {r2.text}\n")
            
        #joiner
        r3 = requests.put('https://www.guilded.gg/api/invites/1EqdAAAp?teamId=JRXQkZBl&', headers={"cookie": f'hmac_signed_session={cookie}'}, proxies=proxy)
        if r3.status_code == 200:
            print(f"> | Succesfully Joined Server: {name}\n")
        else:
            print(f"? | Failed to Join Server\n")
            
        #saving
        f = open(f'Guilded-Cookies.txt', "a+");f.write(f'{cookie}\n');f.close()

    except Exception:
        try:
            proxies.remove(proxy)
        except:
            pass
        print(f'{Fore.RESET}Ratelimited')

def start():
    while True:
        N = 7
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        create(f'Guilded.rip | {res}', f'bottedaccount+{res}@gmail.com', f'{res}{res}')

def threaded():
    print("Logging in...\n")
    threads = []
    for i in range(20):
        t = Thread(target=start, daemon=True)
        t.start()
        threads.append(t)
    for thread in threads:
        t.join()

if __name__ == "__main__":
    os.system('cls')
    threaded()
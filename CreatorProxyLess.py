import requests
import random
import string
import threading
import os
from threading import Thread
from colorama import Fore, Style, init

#https://www.guilded.gg/api/invites/42DOaQ7E?teamId=Oj1oeMpl&

webhook = "https://media.guilded.gg/webhooks/9482deda-f59f-4dea-9fd4-af8ff12727b8/yCDS1D0yTmygEmsuasSiEoqUQuGwWa8KIswoOKYCKccI6AAaOCkwU4WcMISWOA6EyM4OkSmY0MeoKOgAsaa2WC"

def create(name, email, password):
    try:
        #creator
        requests.post('https://www.guilded.gg/api/users?type=email', headers={'Content-Type': 'application/json','guilded-client-id': '17119702-e1c6-4d8f-8920-4f7ca425b84d', 'guilded-device-id': '537b5c96c662685a3c6a9cf97b15fafe68ca4eb5141254ac908d08f4460218cc', 'guilded-device-type': 'desktop', 'guilded-stag': '0646ede6507f50ace615efb1c9d14b48','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153'}, json = {'name': name, 'email': email, 'password': password, 'fullName': name})
        r2 = requests.post('https://www.guilded.gg/api/login', json = {'email': email, 'password': password, 'getMe': True})
        cookie = str(r2.cookies).split('hmac_signed_session=')[1].split(' ')[0]
        if r2.status_code == 200:
            print(f"\u001b[38;5;213m> | Succesfully Created New Account: {cookie}\n")
        else:
            print(f"\u001b[38;5;196m? | Failed to Create Account: {r2.text}\n")
            
        #joiner
        r3 = requests.put('https://www.guilded.gg/api/invites/42DOaQ7E?teamId=N3EaX7j3&', headers={"cookie": f'hmac_signed_session={cookie}'})
        if r3.status_code == 200:
            print(f"\u001b[38;5;213m> | Succesfully Joined Server: {cookie}\n")
        else:
            print(f"\u001b[38;5;196m? | Failed to Join Server\n")
            
        #webhook
        requests.post(webhook, json={"content": cookie})

        #saving
        f = open(f'Guilded-Cookies.txt', "a+");f.write(f'{cookie}\n');f.close()

    except Exception: print("\u001b[38;5;213mRatelimited")

def start():
    while True:
        N = 7
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        create(f'Guilded.rip | {res}', f'bottedaccount+{res}@gmail.com', f'{res}{res}')

def threaded():
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
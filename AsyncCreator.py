import random
import string
import asyncio
import aiohttp

async def create(name, password, email):
    try:
        async with aiohttp.ClientSession(headers={'Content-Type': 'application/json','guilded-client-id': '17119702-e1c6-4d8f-8920-4f7ca425b84d', 'guilded-device-id': '537b5c96c662685a3c6a9cf97b15fafe68ca4eb5141254ac908d08f4460218cc', 'guilded-device-type': 'desktop', 'guilded-stag': '0646ede6507f50ace615efb1c9d14b48','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 OPR/78.0.4093.153'}) as session:
            async with session.post("https://www.guilded.gg/api/users?type=email", json = {'name': name, 'email': email, 'password': password, 'fullName': name}) as r:
                async with session.post('https://www.guilded.gg/api/login', json = {'email': email, 'password': password, 'getMe': True}) as r2:
                    cookie = str(r2.cookies).split('hmac_signed_session=')[1].split(' ')[0]
                    if r2.status == 200:
                        print(f"> | Succesfully Created New Account: {name}\n")
    except Exception:
        print("Ratelimited")


def start():
    while True:
        N = 7
        res = ''.join(random.choices(string.ascii_uppercase + string.digits, k = N))
        loop = asyncio.get_event_loop()
        loop.run_until_complete(create(f'Guilded.rip | {res}', f'bottedaccount+{res}@gmail.com', f'{res}{res}'))

start()
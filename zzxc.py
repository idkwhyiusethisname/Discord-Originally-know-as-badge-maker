#import imp
import requests, colorama, threading, time
from capmonster_python import HCaptchaTask
import random
from colorama import Fore
import tls_client

session = tls_client.Session(
    client_identifier="chrome112",
    random_tls_extension_order=True
)


def _cookies():
    session.get("https://discord.com",)
    cookies = session.cookies.get_dict()
    all = []
    for cookie in cookies:
        real = cookies.get(cookie)
        all.append("{}={}".format(cookie, real))
    return all

def xxx(token,name, chkey):
    cookies = _cookies()
    __dcfduid, __sdcfduid, __cfruid = cookies[0], cookies[1], cookies[2]
    fx = {
    "accept": "*/*",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,th;q=0.9",
    "authorization": token,
    "content-length": "29",
    "content-type": "application/json",
    "cookie": f'{__dcfduid}; {__sdcfduid}; __stripe_mid=2e2490e7-7e33-41a6-8cce-1cac41bf978db268d7; {__cfruid}; locale=en-US',
    "origin": "https://discord.com",
    "referer": "xx",
    "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
    "x-debug-options": "bugReporterEnabled",
    "x-discord-locale": "en-US",
    "x-discord-timezone": "Asia/Bangkok",
    "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTMgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjIuMy4yIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjEwMDk5LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozNDE2MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
    }
    hh = requests.post("https://discord.com/api/v9/users/@me/pomelo", headers=fx,json={"username":name})
    #print(hh.status_code)

    if "captcha_key" in hh.text:
        print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}!{Fore.LIGHTBLACK_EX}] {Fore.LIGHTGREEN_EX}SOLVEING CAPTCHA {Fore.LIGHTBLACK_EX} >> {token[:34]}***********{Fore.RESET}")

        capmonster = HCaptchaTask(chkey)
        task_id = capmonster.create_task("https://discord.com/api/v9/users/@me/pomelo", "b2b02ab5-7dae-4d6f-830e-7b55634c888b")
        result = capmonster.join_task_result(task_id)
        print(result.get("gRecaptchaResponse"))
        fz = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,th;q=0.9",
        "authorization": token,
        "content-length": "29",
        "content-type": "application/json",
        "cookie": f'{__dcfduid}; {__sdcfduid}; __stripe_mid=2e2490e7-7e33-41a6-8cce-1cac41bf978db268d7; {__cfruid}; locale=en-US',
        "origin": "https://discord.com",
        "referer": "xx",
        "sec-ch-ua": "\"Not?A_Brand\";v=\"8\", \"Chromium\";v=\"108\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9013 Chrome/108.0.5359.215 Electron/22.3.2 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
        "x-discord-timezone": "Asia/Bangkok",
        "x-captcha-rqtoken": hh.json()['captcha_rqdata'],
        "x-captcha-key": result.get("gRecaptchaResponse"),
        "x-super-properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDEzIiwib3NfdmVyc2lvbiI6IjEwLjAuMjI2MjEiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV09XNjQpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIGRpc2NvcmQvMS4wLjkwMTMgQ2hyb21lLzEwOC4wLjUzNTkuMjE1IEVsZWN0cm9uLzIyLjMuMiBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMjIuMy4yIiwiY2xpZW50X2J1aWxkX251bWJlciI6MjEwMDk5LCJuYXRpdmVfYnVpbGRfbnVtYmVyIjozNDE2MCwiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbH0=",
        }
        xx = requests.post("https://discord.com/api/v9/users/@me/pomelo", headers=fz,json={"username":name})
        if "captcha_key" in xx.json():
            print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}?{Fore.LIGHTBLACK_EX}] {Fore.RED}CAPTCHA CANT SOLVE SKIPING {Fore.LIGHTBLACK_EX}>> {token[:34]}***********{Fore.RESET}")
        if "username" in xx.json():
            print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}!{Fore.LIGHTBLACK_EX}] {Fore.LIGHTGREEN_EX}{rr.json()['username']} CHANGE GOBAL NAME TO {rr.json()['global_name']} {Fore.LIGHTBLACK_EX} >> {token[:34]}***********{Fore.RESET}")
        else:
            print(xx.json())
    elif "Unauthorized" in hh.text:
        try:
            rr = requests.patch("https://discord.com/api/v9/users/@me", headers=fx, json={"global_name":name})
            if rr.status_code == 200:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.GREEN}!{Fore.LIGHTBLACK_EX}] {Fore.LIGHTGREEN_EX}{rr.json()['username']} CHANGE GOBAL NAME TO {rr.json()['global_name']} {Fore.LIGHTBLACK_EX} >> {token[:34]}***********{Fore.RESET}")
                #print(rr.json())
            else:
                print(f"{Fore.LIGHTBLACK_EX}[{Fore.RED}?{Fore.LIGHTBLACK_EX}] {Fore.RED}DEATH TOKEN OR ERROR {Fore.LIGHTBLACK_EX} >> {token[:34]}*********** {Fore.RESET}")
        except:
            print("ERROR ")

if __name__ == "__main__":
    print(Fore.LIGHTBLUE_EX + ''' 

    ╦═╗╔═╗╔═╗╔═╗╔╗╔═╗ ╦╦ ╦
    ╠╦╝║╣ ║ ╦║╣ ║║║╔╩╦╝╚╦╝ All rights reversed ©
    ╩╚═╚═╝╚═╝╚═╝╝╚╝╩ ╚═ ╩  Discord Badge Maker Code by regenxy 
    ''')
    xxc = input(f"{Fore.LIGHTGREEN_EX} Capmonster Key >> ")
    x = input(f"{Fore.LIGHTGREEN_EX} Names  >> ")
    print("\n")
    with open('tokens.txt', 'r') as f:
        tk = f.read().splitlines()
    for xx in tk:
        threading.Thread(target=xxx, args=(xx,x, xxc)).start()
        time.sleep(0.5)
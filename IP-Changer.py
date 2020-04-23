import os
import time
from colorama import Fore
print ("""
The Python Script For Change Public IP Address Your System 
Coded By AmirHoseinTangsiri
""")
while True:
	time.sleep(3)
	os.system("sudo systemctl reload tor")
	print (Fore.GREEN + "Changed IP")

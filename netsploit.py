import os
import subprocess
import time
import sys
from colorama import Fore, Back, Style
from threading import *
from src.display import *
from src.scan import *
from tqdm import tqdm
from time import sleep
from scapy.all import *
import socket
from src.logo import *
from src.mitm import *


os.system("clear")
print(Style.BRIGHT+Fore.GREEN + print_logo())

out = Output()


if os.geteuid() != 0:
    exit("Run the script as root user. \nPlease try again.........")
else:
    Run = True

out.about_author()

class Netsploit:
    def __init__(self):
        self.path = "netsploit"
        self.targetip = "-"

    def IP_COMPILER(self,IP):
        ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
        if ip_add_pattern.search(IP):
            return True
        else:
            return False


    def get_input(self):
        while Run:
            try:
                cmd = input(Fore.WHITE + Style.BRIGHT +self.path+ Style.RESET_ALL +  " ➜ "  + Fore.WHITE)
                if cmd == "help":
                    if self.path == "netsploit/mitm":
                        out.help_mitm()
                    else:
                        out.out_root()
                elif cmd == "back":
                    if self.path == "netsploit/mitm":
                        self.path = "netsploit"
                    else:
                        pass
                elif cmd == "exit":
                    print(Fore.RED,"Goodbye!!")
                    sys.exit(1)
                elif cmd == "clear":
                    os.system("clear")
                elif cmd == "scan":
                    try:
                        print(Fore.YELLOW+Style.BRIGHT+"Scanning For Live Host......"+Style.RESET_ALL)
                        with tqdm(total=100) as pbar:
                            for i in range(10):
                                sleep(0.1)
                                pbar.update(10)
                        scan = Scanner().scan()
                    except KeyboardInterrupt:
                        print(Fore.RED+Style.BRIGHT+"[!] Scan Aborted....")
                elif cmd == "modules":
                    out.Modules()
                elif cmd == "about":
                    out.about_author()
                elif "mitm" == cmd:
                    self.path = "netsploit/mitm"
                elif cmd == "option" and self.path == "netsploit/mitm":
                    out.option_mitm(targetip=self.targetip)
                elif "set" in cmd:
                    cmd = cmd.split(" ")
                    cmd = cmd[-1]
                    print(cmd)
                    if self.path == "netsploit/mitm":
                        if self.IP_COMPILER(IP=cmd) == True:
                            print(Style.BRIGHT+Fore.GREEN+f"[+] IP => {cmd} is Valid.") 
                            print(Fore.GREEN+Style.BRIGHT+f"[+] Target IP ==>  {cmd}.")
                            self.targetip = cmd
                        else:
                            print(Fore.RED+f"[+] ERROR: Invalid IP => {cmd}")
                        

                else:
                    pass
            except KeyboardInterrupt:
                print(Fore.RED,"Goodbye!!")
                break


Netsploit().get_input()
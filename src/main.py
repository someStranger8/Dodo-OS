import time
import os
import sys
def home():
    os.system("clear")
    print("")
    print("")
    print("        ____            __        ")
    print("       / __ \____  ____/ /___     ")
    print("      / / / / __ \/ __  / __ \    ")
    print("     / /_/ / /_/ / /_/ / /_/ /    ")
    print("    /_____/\____/___,_/\____/ __  ")
    print("            / / / /___ ______/ /__")
    print("           / /_/ / __ `/ ___/ //_/")
    print("          / __  / /_/ / /__/ ,<")   
    print("         /_/ /_/\__,_/\___/_/|_|")  
    print("")                              
    print("")
    print("     [01] DDoS Attack")
    print("     [02] Backdoor Entrance")
    print("     [03] WireShark")
    print("     [04] Spam Attack")
    print("     [05] Phishing Attack")
    print("     [06] Nmap")
    print("     [07] Github")
    print("     [08] Shell")
    print("     [09] Hydra")
    print("     [10] Doomsday wordlist")
    print("     [11] Netcat")
    print("     [12] Darkweb")
    print("     [13] Help")
    print("     [14] Logout")
    print("")
    dodo=input("[*] enter your choice: ")
    if dodo == "1":
        print("")
        ip=input("[*] enter sever domain or ip address: ")
        ping = "ping "+ ip+""
        os.system(ping)
    elif dodo == "2":
        print("")
        user=input("enter targets username: ")
        ip2=input("enter targets ip address: ")
        ssh = "ssh "+ user+"@"+ ip2+""
        os.system(ssh)
    elif dodo == "3":
        print("")
        install = "sudo apt install wireshark -y"
        run = "sudo wireshark"
        os.system(install)
        os.system(run)
    elif dodo == "4":
        print("")
        email=input("[*] enter targets email: ")
        subject=input("[*] enter what the email will say: ")
        spam = "mail -s "+ subject+" "+ email+""
        i=1
        while i < 10:
            os.system(spam)
        i+=1
    elif dodo == "5":
        print("")
        php = "sudo apt install php -y"
        gitclone = "git clone https://github.com/An0nUD4Y/blackeye"
        cd = "cd blackeye"
        chmod = "chmod 777 blackeye.sh"
        start = "blackeye.sh"
        os.system(php)
        os.system(gitclone)
        os.system(cd)
        os.system(chmod)
        os.system(start)
    elif dodo == "6":
        print("")
        nmap=input("[*] enter target domain or ip address: ")
        install2 = "sudo apt install nmap -y"
        run2 = "nmap "+ nmap+""
        os.system(install2)
        os.system(run2)
    elif dodo == "7":
        print("")
        github = "xdg-open https://www.github.com"
        os.system(github)
    elif dodo == "8":
        os.system("clear")
        print("Welcome to Dodo OS Shell")
        print("type exit to go to home")
        i=1
        while i < 10:
            shell=input("dodo@dodo:~$ ")
            if shell == "exit":
                home()
            else:
                os.system(shell)
        i+=1
    elif dodo == "9":
        print("")
        user=input("[*] enter user: ")
        passlist=input("[*] enter wordlist: ")
        ip=input("[*] enter ip address: ")
        hydra = "hydra -l "+ user+" -P "+ passlist+" ftp://"+ ip+""
        os.system(hydra)
    elif dodo == "10":
        print("")
        gitclone = "git clone https://github.com/someStranger8/DoomsDay"
        cd = "cd doomsday"
        nano = "nano doomsday.txt"
        os.system(gitclone)
        os.system(cd)
        os.system(nano)
    elif dodo == "11":
        ip=input("[*] enter ip address: ")
        port=input("[*] enter port number: ")
        install = "sudo apt install netcat -y"
        netcat = "nc -nv "+ ip+" "+ port+""
        os.system(install)
        os.system(netcat)
    elif dodo == "12":
        print("")
        dark = "git clone https://github.com/somestranger8/darkweb"
        cd = "cd darkweb"
        netcat = "sudo apt install netcat"
        web = "python3 main.py"
        os.system(dark)
        os.system(cd)
        os.system(netcat)
        os.system(web)
    elif dodo == "13":
        print("welcome to dodo os")
        print("-" * 13)
        print("dodo os is for pen-testing")
        print("and hacking")
        time.sleep(3)
        home()
    elif dodo == "14":
        print("")
        os.system("sudo apt update")
        login()
def login():
    os.system("clear")
    u=input("enter username >>> ")
    p=input("enter password >>> ")
    if u == "dodo" and p == "dodo":
        home()
    else:
        print("sorry wrong username or password")
        time.sleep(1)
        login()
login()

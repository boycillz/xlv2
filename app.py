# -*- coding: utf-8 -*-
import os
import sys
import time
import base64
from test import *

g = "\033[32;1m"
gt = "\033[0;32m"
bt = "\033[34;1m"
b = "\033[36;1m"
m = "\033[31;1m"
c = "\033[0m"
p = "\033[37;1m"
u = "\033[35;1m"
M = "\033[3;1m"
k = "\033[33;1m"
kt = "\033[0;33m"
a = "\033[30;1m"

try:
    import platform
    from xlpy import *
except Exception as err:
    print (m+"["+k+"Error : "+p+str(err)+m+"]")
    sys.exit()
except KeyboardInterrupt:
	  print (m+"[" + p + "Fail To Import" + m + "]")
	  sys.exit()

tembak = """
{0}  @@@@@@@ @@@@@@@@ @@@@@@@@@@  @@@@@@@   @@@@@@  @@@  @@@
    @@!   @@!      @@! @@! @@! @@!  @@@ @@!  @@@ @@!  !@@
    @!!   @!!!:!   @!! !!@ @!@ @!@!@!@  @!@!@!@! @!@@!@! 
    !!:   !!:      !!:     !!: !!:  !!! !!:  !!! !!: :!! 
     :    : :: :::  :      :   :: : ::   :   : :  :   :::
                       @@@  @@@ @@@     
                       @@!  !@@ @@!     
                        !@@!@!  @!!     
                        !: :!!  !!:     
                       :::  ::: : ::.: :
___________________________________________________________

   {0}Created By :   {1}Albertoanggi
   {0}Edited By  :   {1}Mr.A_S
   {0}Github     :   {1}https://github.com/albertoanggi/xl-py
   {0}Github     :   {1}https://github.com/haijuga7/xl-py2
   {0}Versi      :   {1}2.0
{0}___________________________________________________________
""".format(gt, p)

def main_menu():
    try:
        clear()
        print (tembak)
        print (g+"            ..::XL - Direct Purchase Package::..")
        print (gt+"\nPlease choose the menu you want to start:")
        print (gt+"  ["+p+"1"+gt+"] "+p+"Purchase Package")
        print (gt+"  ["+p+"2"+gt+"] "+p+"Request Password")
        print (gt+"  ["+p+"0"+gt+"] "+p+"Quit")
        choice = str(input(gt+"Choose >> "+p))
        exec_menu(choice)
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        main_menu()

def exec_menu(choice):
    try:
        clear()
        if(choice == ''):
            menu_actions['main']()
        else:
            try:
                menu_actions[choice]()
            except KeyError:
                print("Invalid selection, please try again.\n")
                menu_actions['main']()
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        exec_menu(choice)

def menu_1():
    try:
        print (tembak)
        print(g+"                ..::Purchase Package Menu::..")
        print ("")
        msisdn = str(input(gt+"Input your MSISDN >> "+p))
        passwd = str(input(gt+"Input your password >> "+p))
        print (gt+"___________________________________________________________")
        print ("")
        print (g+"              ..::List Menu Tembak Paket Xl::..")
        print ("")
        print (p+" 01"+gt+") "+p+"Paket Xtra Kuota 30GB Rp. 10.000")
        print (p+" 02"+gt+") "+p+"List Paket Xtra Combo Lite")
        print (p+" 03"+gt+") "+p+"List Paket Xtra Combo Xtra")
        print (p+" 04"+gt+") "+p+"List Paket Xtra Combo Prima")
        print (p+" 05"+gt+") "+p+"List Paket Xtra Kuota Ramadan")
        print (p+" 06"+gt+") "+p+"Xtra Youtube 1 Tahun Rp. 0 (Trial)")
        print (p+" 07"+gt+") "+p+"XL GO IZI 10 GB Rp. 0")
        print (p+" 08"+gt+") "+p+"XTRAGRAM 3GB Rp. 0 (trial)")
        print ("")
        lihat = str(input(gt+"Select one >> "+p))
        if lihat == '1':
            c = b'\xff\xfe8\x001\x001\x000\x005\x007\x007\x00'
        elif lihat == '2':
            print (gt+"___________________________________________________________")
            print ("")
            print (g+"              ..::List Menu Xtra Combo Lite::..")
            print ("")
            print (p+" 01"+gt+") "+p+"Xtra Combo Lite 3GB Rp. 19.000")
            print (p+" 02"+gt+") "+p+"Xtra Combo Lite 5GB Rp. 29.000")
            print (p+" 03"+gt+") "+p+"Xtra Combo Lite 9GB Rp. 49.000")
            print (p+" 04"+gt+") "+p+"Xtra Combo Lite 17GB Rp. 79.000")
            print (p+" 05"+gt+") "+p+"Xtra Combo Lite 25GB Rp. 99.000")
            print ("")
            look = str(input(gt+"Select one >> "+p))
            if look == '1':
                c = b'\xff\xfe8\x002\x001\x000\x008\x008\x002\x00'
            elif look == '2':
                c = b'\xff\xfe8\x002\x001\x000\x008\x008\x003\x00'
            elif look == '3':
                c = b'\xff\xfe8\x002\x001\x000\x008\x008\x004\x00'
            elif look == '4':
                c = b'\xff\xfe8\x002\x001\x000\x008\x008\x005\x00'
            elif look == '5':
                c = b'\xff\xfe8\x002\x001\x000\x008\x008\x006\x00'
        elif lihat == '3':
            print (gt+"___________________________________________________________")
            print ("")
            print (g+"              ..::List Menu Xtra Combo::..")
            print ("")
            print (p+" 01"+gt+") "+p+"Xtra Combo 5GB + 5GB Rp. 59.000")
            print (p+" 02"+gt+") "+p+"Xtra Combo 10GB + 10GB Rp. 89.000")
            print (p+" 03"+gt+") "+p+"Xtra Combo 15GB + 15GB Rp. 129.000")
            print (p+" 04"+gt+") "+p+"Xtra Combo 20GB + 20GB Rp. 179.000")
            print (p+" 05"+gt+") "+p+"Xtra Combo 35GB + 35GB Rp. 239.000")
            print ("")
            ok = str(input(gt+"Select one >> "+p))
            if ok == '1':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x003\x00'
            elif ok == '2':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x004\x00'
            elif ok == '3':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x005\x00'
            elif ok == '4':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x006\x00'
            elif ok == '5':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x007\x00'
        elif lihat == '4':
            print (gt+"___________________________________________________________")
            print ("")
            print (g+"              ..::List Menu Xtra Combo Prima::..")
            print ("")
            print (p+" 01"+gt+") "+p+"Xtra Combo Prima 5GB + 5GB Rp. 69.000")
            print (p+" 02"+gt+") "+p+"Xtra Combo Prima 10GB + 10GB Rp. 99.000")
            print (p+" 03"+gt+") "+p+"Xtra Combo Prima 15GB + 15GB Rp. 139.000")
            print (p+" 04"+gt+") "+p+"Xtra Combo Prima 20GB + 20GB Rp. 189.000")
            print (p+" 05"+gt+") "+p+"Xtra Combo Prima 35GB + 35GB Rp. 249.000")
            print ("")
            pok = str(input(gt+"Select one >> "+p))
            if pok == '1':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x008\x00'
            elif pok == '2':
                c = b'\xff\xfe8\x002\x001\x001\x001\x008\x009\x00'
            elif pok == '3':
                c = b'\xff\xfe8\x002\x001\x001\x001\x009\x000\x00'
            elif pok == '4':
                c = b'\xff\xfe8\x002\x001\x001\x001\x009\x001\x00'
            elif pok == '5':
                c = b'\xff\xfe8\x002\x001\x001\x001\x009\x002\x00'
        elif lihat == '5':
            print (gt+"___________________________________________________________")
            print ("")
            print (g+"              ..::List Menu Xtra Kuota Ramadan::..")
            print ("")
            print (p+" 01"+gt+") "+p+"Waze & Chat 1 Day Rp. 500")
            print (p+" 02"+gt+") "+p+"Waze & Chat 3 Day Rp. 1000")
            print (p+" 03"+gt+") "+p+"Waze & Chat 7 Day Rp. 2500")
            print (p+" 04"+gt+") "+p+"Facebook & Chat 1 Day [14:00-19:00] Rp. 500")
            print (p+" 05"+gt+") "+p+"Facebook & Chat 3 Day [14:00-19:00] Rp. 1000")
            print (p+" 06"+gt+") "+p+"Facebook & Chat 7 Day [14:00-19:00] Rp. 2500")
            print (p+" 07"+gt+") "+p+"Instagram & Chat 1 Day [14:00-19:00] Rp. 500")
            print (p+" 08"+gt+") "+p+"Instagram & Chat 3 Day [14:00-19:00] Rp. 1000")
            print (p+" 09"+gt+") "+p+"Instagram & Chat 7 Day [14:00-19:00] Rp. 2500")
            print (p+" 10"+gt+") "+p+"Streaming & Chat 1 Day [14:00-19:00] Rp. 500")
            print (p+" 11"+gt+") "+p+"Streaming & Chat 3 Day [14:00-19:00] Rp. 1000")
            print (p+" 12"+gt+") "+p+"Streaming & Chat 7 Day [14:00-19:00] Rp. 2500")
            print (p+" 13"+gt+") "+p+"Facebook & Chat 1 Day [01:00-06:00] Rp. 500")
            print (p+" 14"+gt+") "+p+"Facebook & Chat 3 Day [01:00-06:00] Rp. 1000")
            print (p+" 15"+gt+") "+p+"Facebook & Chat 7 Day [01:00-06:00] Rp. 2500")
            print (p+" 16"+gt+") "+p+"Instagram & Chat 1 Day [01:00-06:00] Rp. 500")
            print (p+" 17"+gt+") "+p+"Instagram & Chat 3 Day [01:00-06:00] Rp. 1000")
            print (p+" 18"+gt+") "+p+"Instagram & Chat 7 Day [01:00-06:00] Rp. 2500")
            print (p+" 19"+gt+") "+p+"Streaming & Chat 1 Day [01:00-06:00] Rp. 500")
            print (p+" 20"+gt+") "+p+"Streaming & Chat 3 Day [01:00-06:00] Rp. 1000")
            print (p+" 21"+gt+") "+p+"Streaming & Chat 7 Day [01:00-06:00] Rp. 2500")
            print ("")
            dor = str(input(gt+"Select one >> "+p))
            if dor == '1':
                c = b'\xff\xfe8\x002\x001\x001\x003\x006\x009\x00'
            elif dor == '2':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x000\x00'
            elif dor == '3':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x001\x00'
            elif dor == '4':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x008\x00'
            elif dor == '5':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x009\x00'
            elif dor == '6':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x000\x00'
            elif dor == '7':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x002\x00'
            elif dor == '8':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x003\x00'
            elif dor == '9':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x004\x00'
            elif dor == '10':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x004\x00'
            elif dor == '11':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x005\x00'
            elif dor == '12':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x006\x00'
            elif dor == '13':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x001\x00'
            elif dor == '14':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x002\x00'
            elif dor == '15':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x003\x00'
            elif dor == '16':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x005\x00'
            elif dor == '17':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x006\x00'
            elif dor == '18':
                c = b'\xff\xfe8\x002\x001\x001\x003\x007\x007\x00'
            elif dor == '19':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x007\x00'
            elif dor == '20':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x008\x00'
            elif dor == '21':
                c = b'\xff\xfe8\x002\x001\x001\x003\x008\x009\x00'
        elif lihat == '6':
            c = b'\xff\xfe8\x002\x001\x000\x009\x004\x009\x00'
        elif lihat == '7':
            c = b'\xff\xfe8\x002\x001\x001\x002\x003\x001\x00'
        elif lihat == '8':
            c = b'\xff\xfe8\x001\x001\x000\x006\x002\x004\x00'
        serviceid = c.decode('utf-16')
        xl = XL(msisdn)
        r = xl.loginWithPassword(passwd)
        if(r != False):
            print(xl.purchasePackage(serviceid)['message'])
            print (gt+"___________________________________________________________")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            decision = decision.lower()
            if decision == 'y':
                me(msisdn, passwd)
            else:
                main_menu()
        else:
            print(kt+"["+p+"!"+kt+"] "+m+"Login failed try again")
            print (gt+"___________________________________________________________")
            decision = str(input("Want to repeat the process [Y/N]? >> "))
            decision = decision.lower()
            if decision == 'y':
                me(msisdn, passwd)
            else:
                main_menu()
        return

    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        menu_1()
        
def menu_2():
    try:
        clear()
        print (tembak)
        print(g+"               ..::Request Password Menu::..")
        print ("")
        msisdn = str(input(gt+"Input your MSISDN >> "+p))
        xl = XL(msisdn)
        print(xl.reqPassword()['message'])
        print (gt+"___________________________________________________________")
        decision = str(input("Want to repeat the process [Y/N]? >> "))
        menu_actions['main']() if(decision in ['N','n']) else menu_2()
        return
    except(KeyboardInterrupt):
        print (m+"     ["+p+"!"+m+"] "+m+"(Ctrl + C ) Detected, "+p+"Trying To Back ...")
        print (m+"     ["+p+"*"+m+"] "+g+"Thank For Using my Pentest Tools ^~^")
        time.sleep(1)
        menu_2()
    
def exit():
    sys.exit()

def clear():
    return os.system("cls") if (platform.system() == 'Windows') else os.system("clear")

menu_actions = {
    "main" : main_menu,
    "1" : menu_1,
    "2" : menu_2,
    "0" : exit
}


if __name__ == "__main__":
    try:
        main_menu()
    except Exception as err:
        os.system('pip install --upgrade pip')
        os.system('pip install requests')
        os.system('pip install -r requirements.txt')
        os.system('python app.py')

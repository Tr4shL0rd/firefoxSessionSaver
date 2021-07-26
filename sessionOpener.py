import os
from platform import uname

debug = False
if debug == True: print("Debug Mode True")

#Detects OS
def in_wsl() -> bool:
    return "Microsoft" in uname().release
def in_nt() -> bool:
    return "nt" in os.name
def in_nix() -> bool:
    return "posix" in os.name
if debug == True: print("wsl? {}\nnt? {}\nnix? {}".format(in_wsl(),in_nt(),in_nix()))


#Sets Firefox Path Depending on the OS
if in_wsl() == True & in_nix() == True:
    FFPATH = "/mnt/c/'Program Files'/'Mozilla Firefox'/./firefox.exe"
if in_nt() == True:
    FFPATH = "C:/'Program Files'/'Mozilla Firefox'/firefox.exe"
if in_nix() == True & in_wsl() == False:
    FFPATH = "/usr/bin/firefox"

if debug == True: print("FF PATH:",FFPATH)
#Cleaning up path for checking
PathCheck = FFPATH.replace("'", "")
if os.path.isfile(PathCheck) == False:
    print("Cant Find firefox.exe!")
    exit()
if debug == True:
    if "mnt" in FFPATH:
        print("USING WSL")
    elif "C:" in FFPATH:
        print("USING NT")
    else:
        print("USING NIX")
#lists the urls and askes if they should be opened
try:
    f = open("urlListFile.txt", "r")
    url = f.readlines()

    print("######### {} URLS #########".format(len(url)))
    for i in range(len(url)):
        print(url[i])
    print("###########################")
    yn = input("open URLS?(y/n):  ".format(len(url))).lower()

    if yn == "y":
        if debug == False:
            for urlList in range(len(url)):
                os.system("{} {}".format(FFPATH,url[urlList]))
        else:
            for i in range(len(url)):
                print("opened {}".format(url[i]))
except KeyboardInterrupt:
    print("\n#### EXITING ####")
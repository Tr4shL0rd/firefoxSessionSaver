import webbrowser as wb
from platform import uname

debug = False
if debug == True: print("Debug Mode True")

try:
    f = open("urlListFile.txt", "r")
    url = f.readlines()

    print(f"######### {len(url)} URLS #########")
    for i in range(len(url)):
        print(url[i])
    print("###########################")
    yn = input("open URLS?(Y/n):  ").lower()

    if yn == "y" or yn == "":
        if debug == False:
            for urlList in range(len(url)):
                wb.get("firefox").open(url[urlList])
        else:
            for i in range(len(url)):
                print(f"opened {url[i]}")
except KeyboardInterrupt:
    print("\n#### EXITING ####")
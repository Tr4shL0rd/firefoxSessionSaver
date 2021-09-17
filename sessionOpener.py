import webbrowser as wb

f = open("urlListFile.txt", "r")
url = f.readlines()

print(f"######### {len(url)} URLS #########")
for URL in url:
    print(URL)
print("###########################")
yn = input("open URLS?(Y/n): ").lower()

if yn == "y" or yn == "":
    for urlList in url:
        wb.get("firefox").open(urlList)

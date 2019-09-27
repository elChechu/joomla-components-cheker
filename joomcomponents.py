import sys
import requests
import time

data = []
f = open("data.txt", "r")
data = f.readlines()
f.close

# get url param
x = -1
for i in sys.argv:
    x = x + 1 
    if i == "--url":
        url = sys.argv[x+1]
        if url[len(url)-1] != "/":
            url = url + "/"

# check status code
if url != None:
    for i in data:
        if requests.get(url+i) == "200":
            print("[!] Componente: " + i + " Existe")
            time.sleep(0.3)
        else:
            print("[-] Componente: " + i + "No existe")
            time.sleep(0.6)


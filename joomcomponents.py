import sys
import requests
import time

data = []
f = open("data.txt", "r")
data = f.readlines()
f.close



x = -1
for i in sys.argv:
    x = x + 1 
    if i == "--url":
        url = sys.argv[x+1]
        if url[len(url)-1] != "/":
            url = url + "/"



if url != None:
    for i in data:
        if requests.get(url+i) == "200":
            print("existe")
            time.sleep(0.5)
        else:
            print(i+" no existe")
            time.sleep(0.5)


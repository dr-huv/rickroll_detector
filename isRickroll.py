import requests
from bs4 import BeautifulSoup

eurl =input("Enter URL to test\n")
try:
    response = requests.get(eurl)
    soup = BeautifulSoup(response.content, 'html.parser')

    h_dump = str(response.content.decode()).split('\n')

except:
    print("invalid URL")
    exit()

rick_bool = False

for x in h_dump:
    if "dQw4w9WgXcQ" in x:
        rick_bool = True        

if rick_bool:
    print("THIS IS DEFINITELY A RICK ROLL")

else:
    print("link is safe")
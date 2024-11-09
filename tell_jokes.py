from urllib import request
import json
import pyttsx3

f='y'
while f=='y':
    url = "https://official-joke-api.appspot.com/random_joke"
    r = request.urlopen(url)
    data = r.read()
    jsonData = json.loads(data)

    setup = jsonData["setup"]
    punchline = jsonData["punchline"]

    print(setup,punchline)
    pyttsx3.speak([setup,punchline])
    f=input("Do you need another (y/n): ")
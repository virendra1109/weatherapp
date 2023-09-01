import requests
import json
import pyttsx3

engine = pyttsx3.init()       #using for speaker
city = input("Enter the name of your city\n")
url = f"https://api.weatherapi.com/v1/current.json?key=1e70fe0175654e2c9b4191941232508&q={city}"

r = requests.get(url)
wdic = json.loads(r.text)    #This json.loads function converts the string type url to dictionary

sample = wdic['current']['temp_c']
print(sample)
engine.say(sample)
engine.runAndWait()
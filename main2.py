import requests
import json

while True:
    city = input("Enter the name of your city: ")
    if city =="exit":
        break
    url = f"http://api.weatherapi.com/v1/current.json?key=9a3ad472d2c44b33bd045450232912&q={city}"
    a = requests.get(url)

    weather = json.loads(a.text)
    try:
        Temperature = weather["current"]["temp_c"] 
        location = weather["location"]["name"]
        region = weather["location"]["region"]
        country = weather["location"]["country"]
        print(Temperature , location , region ,country)
    except:
        error = weather["error"]["message"]
        print(error)
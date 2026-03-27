# SEGURA Mickael


import requests


url= "http://api.open-notify.org/astros.json"
res = requests.get(url)

#[print(f"{elm["name"]}\n") for elm in res.json()["people"]]

l = [elm["name"] for elm in res.json()["people"] if elm["craft"] == "ISS"]
print(l)
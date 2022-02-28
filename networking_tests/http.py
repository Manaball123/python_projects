import requests



req = requests.get("https://www.w3schools.com/python/module_requests.asp")


print(req.text)
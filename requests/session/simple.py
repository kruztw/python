import requests

s = requests.session()
r = s.get("http://www.example.com")
print(r)

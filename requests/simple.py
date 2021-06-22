import requests

res = requests.get('http://www.example.com', cookies={'key':'value'})
res = requests.post('http://www.example.com', data={'key':'value'})
print(res.text)



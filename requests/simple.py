import requests

try:
    res = requests.get('http://www.example.com', cookies={'key':'value'})
    res = requests.post('http://www.aexample.com', data={'key':'value'})
    res.raise_for_status()
except Exception as err:
    print(f'HTTP error occurred: {err}')

print(res.text)



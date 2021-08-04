import urllib.parse

url = "http://localhost:8080 lalala/abcd/efgh/?a=1&b=2#comment"

print(urllib.parse.urlparse(url))

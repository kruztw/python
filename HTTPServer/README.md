# How to run ?

```=python3

# Terminal1
python3 simple.py



# Terminal2
curl http://localhost:6666 -v



*   Trying 127.0.0.1:6666...
* TCP_NODELAY set
* Connected to localhost (127.0.0.1) port 6666 (#0)
> GET / HTTP/1.1
> Host: localhost:6666
> User-Agent: curl/7.68.0
> Accept: */*
> 
* Mark bundle as not supporting multiuse
* HTTP 1.0, assume close after body
< HTTP/1.0 302 Found
< Server: BaseHTTP/0.6 Python/3.8.10
< Date: Wed, 08 Dec 2021 11:55:30 GMT
< Location: 8888
< 
* Closing connection 0


```

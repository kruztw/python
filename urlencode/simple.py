from urllib.parse import urlencode, quote, unquote
 
data={"key1":"val1","key2":"val2"}

encode = urlencode(data)
print(encode)

encode = quote("/?arg1=val1")
print(encode)


decode = unquote(encode)
print(decode)






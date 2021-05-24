import json

print(None==None)
print(None=={})
print(None==[])
print(None=="")
print(None=="None")

users_db = {
    'guest': 'guest',
}

print(users_db.get("foo") == None)


dic = {"key":None}
print(dic['key'] == None)


dic = '{"key":null}'
json_dic = json.loads(dic)
print(json_dic['key'] == None)

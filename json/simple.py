import json
import ujson

data = '{"foo":"bar", "123":null}'
print(json.loads(data))
print(ujson.loads(data))       # ultra json: 快速版的 json

import getPDI

import json

data = getPDI.getPDI()
print("DATA:",data)

print(type(data))

json_obj = json.loads(data)

print(type(json_obj))

print(json_obj['pdi'])
print(json_obj['url'])
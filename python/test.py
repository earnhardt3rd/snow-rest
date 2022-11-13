import getPDI, getAPI

import json

pdi_str = getPDI.getPDI()
print("DATA:",pdi_str)
print(type(pdi_str))
pdi_json = json.loads(pdi_str)
print(type(pdi_json))
print(pdi_json['pdi'])
print(pdi_json['url'])

api_str = getAPI.getAPI()
api_json = json.loads(api_str)
print(api_json['api'])
print(api_json['uri'])

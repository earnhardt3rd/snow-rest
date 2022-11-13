import sys,json
MIN_PYTHON = (3, 0)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

def getAPI() :
  f = open('../rest_api.json')
  data = json.load(f)
  f.close()
  y=0
  pdi = []
  for x in data['api_details']:
    pdi.append(x)
    y = y + 1
    print('  ',str(y),"api:",x['api'].ljust(30,' '),"  --uri:",x['uri'])

  ans = str(input("  Enter API number? (x~exit)[1]:"))
  if ans == '':
    ans=1

  if str(ans).isalpha():
    print("Good-bye")
  else:
    # print(data['pdi_details'][ans-1])
    return json.dumps(data['api_details'][int(ans) - 1])
if __name__ == "__main__":
  rtn_str = getAPI()
  print('  RTN_STR:',rtn_str)
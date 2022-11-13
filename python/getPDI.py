import sys,json
MIN_PYTHON = (3, 0)
if sys.version_info < MIN_PYTHON:
    sys.exit("Python %s.%s or later is required.\n" % MIN_PYTHON)

def getPDI() :
  f = open('../pdi.json')
  data = json.load(f)
  #print("JSON string=", data)

  # for i in data['pdi_details']:
  #   print(i)

  f.close()

  # json_hash = {
  #   "first_name" : "joe",
  #   "last_name" : "doer",
  #   "email" : "joe.doer@gmail.com"
  # }

  # json_obj = json.dumps(json_hash, indent=4)
  # print(json_obj)

  # with open("../json_hash.json", "w") as outfile:
  #   outfile.write(json_obj)
  y=0
  pdi = []
  for x in data['pdi_details']:
    pdi.append(x)
    y = y + 1
    print(str(y),"pdi:",x['pdi'].ljust(30,' '),"  --url:",x['url'])

  ans = str(input("  Enter PDI number? (x~exit)[1]:"))
  if ans == '':
    ans = 1

  if str(ans).isalpha():
    print("Good-bye")
  else:
    # print(data['pdi_details'][ans-1])
    return json.dumps(data['pdi_details'][int(ans) - 1])
if __name__ == "__main__":
  rtn_str = getPDI()
  print('  RTN_STR:',rtn_str)
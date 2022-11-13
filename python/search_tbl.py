import sys, getopt, json
import requests
import getPDI, getAPI

pdi_str = getPDI.getPDI()
pdi_json = json.loads(pdi_str)
print(pdi_json['pdi'])
print(pdi_json['url'])

api_str = getAPI.getAPI()
api_json = json.loads(api_str)
print(api_json['api'])
print(api_json['uri'])

url=pdi_json['url']
uri=api_json['uri']
user=pdi_json['user']
pwd=pdi_json['pwd']
limit='100'
suppress_pagination='true'
query=''
rtn_flds=''
server=''
def usage():
  print('  Help:')
  print('  ',sys.argv[0], ' -s <Server> -l <Limit> -u <User> -p <Pass> -t <Table> -f <Field>')
  print('  ')
  sys.exit()
def main(argv):
  global server
  global limit
  global user
  global pwd
  global query
  global rtn_flds

  try:
    opts, args = getopt.getopt(argv, 'hs:l:u:p:q:r:')
  except getopt.GetoptError:
    usage()
  for opt, arg in opts:
    print('  opt==',opt, ' :: arg==', arg)
    if opt == '-h':
      usage()
    elif opt in ('-s'):
      print('  --set server=',arg)
      server = arg
    elif opt in ('-l'):
      print('  --set limit=',arg)
      limit = arg
    elif opt in ('-u'):
      print('  --set usernm=',arg)
      user = arg
    elif opt in ('-p'):
      print('  --set pass=',arg)
      pwd = arg
    elif opt in ('-q'):
      print('  --set query=',arg)
      query= arg
    elif opt in ('-r'):
      print('  --set rtn_flds=',arg)
      rtn_flds= arg

if __name__ == '__main__':
  main(sys.argv[1:])
print('  ============================')
print('  Number of arguments:', len(sys.argv), 'arguments.')
print('  Argument List:', str(sys.argv))
print('  ============================')
print('  Server:', server)
print('  User:', user)
print('  Pass:', pwd)
print('  Query:', query)
print('  RtnFlds:', rtn_flds)
# Set the request parameters
url = url + uri
if rtn_flds != '':
  url = url + '&sysparm_fields=' + rtn_flds

print('  URL:', url)

# Set proper headers
headers = {'Content-Type':'application/json','Accept':'application/json'}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200:
  print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
  exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
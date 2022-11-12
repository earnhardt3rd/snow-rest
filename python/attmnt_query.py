#Need to install requests package for python
#easy_install requests
import requests
import sys, getopt

server="dev77308.service-now.com"
user="admin"
pwd="tu!Zo1oUQ-5Q"
limit="1"
suppress_pagination="true"
rtn_flds=""

codes = {'=' : '%3D', '^' : '%5E'}
for k in codes:
  print("  key:",k," val:",codes[k])
# = %3D
# ^ %5E
menu = []
menu.append("table_name=incident^file_nameSTARTSWITHACME")
menu.append("file_name=ACME_logo1.png")
menu.append("table_name=incident")

i=0
for q in menu:
  i = i + 1
  print('  ' + str(i) + '  :' + menu[i-1])

ans = int(input("  Enter a choice: "))
query = menu[ans-1]

def main(argv):
  global server
  global limit
  global user
  global pwd
  global query
  global rtn_flds


  try:
    opts, args = getopt.getopt(argv, "hs:l:u:p:q:r:")
  except getopt.GetoptError:
    print("Error", sys.argv[0], " -u <User> -p <Pass> -t <Table> -f <Field>")
    sys.exit(2)
  for opt, arg in opts:
    print("  opt==",opt, " :: arg==", arg)
    if opt == "-h":
      print("  Help:")
      print("  ",sys.argv[0], " -u <User> -p <Pass> -t <Table> -f <Field>")
      sys.exit()
    elif opt in ("-s"):
      print("  --set server=",arg)
      server = arg
    elif opt in ("-l"):
      print("  --set limit=",arg)
      limit = arg
    elif opt in ('-u'):
      print("  --set usernm=",arg)
      user = arg
    elif opt in ("-p"):
      print("  --set pass=",arg)
      pwd = arg
    elif opt in ("-q"):
      print("  --set query=",arg)
      query= arg
    elif opt in ("-r"):
      print("  --set rtn_flds=",arg)
      rtn_flds= arg

if __name__ == "__main__":
  main(sys.argv[1:])
print("  ============================")
print("  Number of arguments:", len(sys.argv), "arguments.")
print("  Argument List:", str(sys.argv))
print("  ============================")
print("  Server:", server)
print("  User:", user)
print("  Pass:", pwd)
print("  Query:", query)
print("  RtnFlds:", rtn_flds)
# Set the request parameters
url = 'https://' + server + '/api/now/attachment?sysparm_query=' + query + '&sysparm_suppress_pagination_header=' + suppress_pagination + '&sysparm_limit=' + limit
if rtn_flds != "":
  url = url + '&sysparm_fields=' + rtn_flds

print("  URL:", url)

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.get(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
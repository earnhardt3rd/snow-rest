#Need to install requests package for python
#easy_install requests
import requests
import sys, getopt

server="dev77308.service-now.com"
user="admin"
pwd="tu!Zo1oUQ-5Q"
table="customer_account"
field="account_path"

def main(argv):
  global server
  global user
  global pwd
  global table
  global field
  try:
    opts, args = getopt.getopt(argv, "hs:u:p:t:f:")
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
    elif opt in ("-p"):
      print("  --set pass=",arg)
      pwd = arg
    elif opt in ("-t"):
      print("  --set table=",arg)
      table = arg
    elif opt in ("-f"):
      print("  --set field=",arg)
      field = arg
    elif opt in ('-u'):
      print("  --set usernm=",arg)
      user = arg

if __name__ == "__main__":
  main(sys.argv[1:])
print("  ============================")
print("  Number of arguments:", len(sys.argv), "arguments.")
print("  Argument List:", str(sys.argv))
print("  ============================")
print("  Server:", server)
print("  User:", user)
print("  Pass:", pwd)
print("  Table:", table)
print("  Field:", field)
# Set the request parameters
url = 'https://' + server + '/api/sn_cmdb_ws/cmdb_workspace_api_scoped/getfieldtype/' + table + '/' + field
print("  URL",url)


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
#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://tac10058.service-now.com/api/now/table/cmdb/<SYSID>?sysparm_fields=support_group%2Csys_tags%2Clocation&sysparm_input_display_value=%3CGROUP%3E%2C%3CTAG%3E%2C%3CLOCATION%3E'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'admin'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.patch(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
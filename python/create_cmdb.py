#Need to install requests package for python
#easy_install requests
import requests

# Set the request parameters
url = 'https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=sys_class_name%2Cmanufacturer%2Cpo_number%2Csys_domain%2Ccompany%2Cjustification%2Cdepartment%2Cinvoice_number%2Casset_tag%2Cserial_number%2Cmodel_id%2Csupport_group%2Cinstall_status%2Ccost_center%2Csupported_by%2Cname%2Clocation%2Casset'

# Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'admin'

# Set proper headers
headers = {"Content-Type":"application/json","Accept":"application/json"}

# Do the HTTP request
response = requests.post(url, auth=(user, pwd), headers=headers )

# Check for HTTP codes other than 200
if response.status_code != 200: 
    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
    exit()

# Decode the JSON response into a dictionary and use the data
data = response.json()
print(data)
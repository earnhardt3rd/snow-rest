var request = new sn_ws.RESTMessageV2();
request.setEndpoint('https://tac10058.service-now.com/api/now/table/cmdb/<SYSID>?sysparm_fields=support_group%2Csys_tags%2Clocation&sysparm_input_display_value=%3CGROUP%3E%2C%3CTAG%3E%2C%3CLOCATION%3E');
request.setHttpMethod('PATCH');

//Eg. UserName="admin", Password="admin" for this code sample.
var user = 'admin';
var password = 'admin';

request.setBasicAuth(user,password);
request.setRequestHeader("Accept","application/json");

var response = request.execute();
gs.log(response.getBody());
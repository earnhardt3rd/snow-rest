var request = new sn_ws.RESTMessageV2();
request.setEndpoint('https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=name%2Casset%2Cinstall_status%2Cmodel_id%2Cserial_number%2Casset_tag%2Csys_id%2Cmanaged_by&sysparm_limit=10');
request.setHttpMethod('GET');

//Eg. UserName="admin", Password="admin" for this code sample.
var user = 'admin';
var password = 'admin';

request.setBasicAuth(user,password);
request.setRequestHeader("Accept","application/json");

var response = request.execute();
gs.log(response.getBody());
var request = new sn_ws.RESTMessageV2();
request.setEndpoint('https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=sys_class_name%2Cmanufacturer%2Cpo_number%2Csys_domain%2Ccompany%2Cjustification%2Cdepartment%2Cinvoice_number%2Casset_tag%2Cserial_number%2Cmodel_id%2Csupport_group%2Cinstall_status%2Ccost_center%2Csupported_by%2Cname%2Clocation%2Casset');
request.setHttpMethod('POST');

//Eg. UserName="admin", Password="admin" for this code sample.
var user = 'admin';
var password = 'admin';

request.setBasicAuth(user,password);
request.setRequestHeader("Accept","application/json");

var response = request.execute();
gs.log(response.getBody());
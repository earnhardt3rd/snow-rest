var requestBody = ""; 

var client=new XMLHttpRequest();
client.open("post","https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=sys_class_name%2Cmanufacturer%2Cpo_number%2Csys_domain%2Ccompany%2Cjustification%2Cdepartment%2Cinvoice_number%2Casset_tag%2Cserial_number%2Cmodel_id%2Csupport_group%2Cinstall_status%2Ccost_center%2Csupported_by%2Cname%2Clocation%2Casset");

client.setRequestHeader('Accept','application/json');
client.setRequestHeader('Content-Type','application/json');

//Eg. UserName="admin", Password="admin" for this code sample.
client.setRequestHeader('Authorization', 'Basic '+btoa('admin'+':'+'admin'));

client.onreadystatechange = function() { 
	if(this.readyState == this.DONE) {
		document.getElementById("response").innerHTML=this.status + this.response; 
	}
}; 
client.send(requestBody);
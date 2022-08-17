var requestBody = ""; 

var client=new XMLHttpRequest();
client.open("get","https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=name%2Casset%2Cinstall_status%2Cmodel_id%2Cserial_number%2Casset_tag%2Csys_id%2Cmanaged_by&sysparm_limit=10");

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
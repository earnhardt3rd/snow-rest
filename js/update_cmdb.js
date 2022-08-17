var requestBody = ""; 

var client=new XMLHttpRequest();
client.open("patch","https://tac10058.service-now.com/api/now/table/cmdb/<SYSID>?sysparm_fields=support_group%2Csys_tags%2Clocation&sysparm_input_display_value=%3CGROUP%3E%2C%3CTAG%3E%2C%3CLOCATION%3E");

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
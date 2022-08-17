 #!/usr/bin/env ruby
 
 require 'base64'
 
 # https://rubygems.org/gems/json
 # Example install using gem
 #   gem install json
 require 'json'
 
 # https://rubygems.org/gems/rest-client
 # Example install using gem
 #   gem install rest-client
 require 'rest_client'
 
 # Set the request parameters
 url = 'https://tac10058.service-now.com/api/now/table/cmdb?sysparm_fields=sys_class_name%2Cmanufacturer%2Cpo_number%2Csys_domain%2Ccompany%2Cjustification%2Cdepartment%2Cinvoice_number%2Casset_tag%2Cserial_number%2Cmodel_id%2Csupport_group%2Cinstall_status%2Ccost_center%2Csupported_by%2Cname%2Clocation%2Casset'
 
 # Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'admin'

request_body_map = "";
 
 begin
   response = RestClient.post("#{url}", 
                              {:authorization => "Basic #{Base64.strict_encode64("#{user}:#{pwd}")}",
                              
                              :accept => 'application/json'
                              })
   puts "#{response.to_str}"
   puts "Response status: #{response.code}"
   response.headers.each { |k,v|
     puts "Header: #{k}=#{v}"
   }
 
 rescue => e
   puts "ERROR: #{e}"
 end
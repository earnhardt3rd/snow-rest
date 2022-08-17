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
 url = 'https://tac10058.service-now.com/api/now/table/cmdb/<SYSID>?sysparm_fields=support_group%2Csys_tags%2Clocation&sysparm_input_display_value=%3CGROUP%3E%2C%3CTAG%3E%2C%3CLOCATION%3E'
 
 # Eg. User name="admin", Password="admin" for this code sample.
user = 'admin'
pwd = 'admin'

request_body_map = "";
 
 begin
   response = RestClient.patch("#{url}", 
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
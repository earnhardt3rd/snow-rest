 #!/usr/bin/env perl -w
 use strict;
 use warnings;
 use MIME::Base64;
 
 # http://search.cpan.org/~makamaka/JSON/lib/JSON.pm
 # Example install using cpanm:
 #   sudo cpanm -i JSON
 use JSON;
 
 # http://search.cpan.org/~mcrawfor/REST-Client/lib/REST/Client.pm
 # Example install using cpanm:
 #   sudo cpanm -i REST::Client
 use REST::Client;
 
 # Set the request parameters
 my $host = 'https://tac10058.service-now.com';
 
 # Eg. User name="admin", Password="admin" for this code sample.
 my $user = 'admin';
 my $pwd = 'admin';

 
 my $client = REST::Client->new(host => $host);
 
 my $encoded_auth = encode_base64("$user:$pwd", '');
 
 $client->GET("/api/now/table/cmdb?sysparm_fields=name%2Casset%2Cinstall_status%2Cmodel_id%2Cserial_number%2Casset_tag%2Csys_id%2Cmanaged_by&sysparm_limit=10",
                
                {'Authorization' => "Basic $encoded_auth",
                 
                 'Accept' => 'application/json'}); 
 
 print 'Response: ' . $client->responseContent() . "\n";
 print 'Response status: ' . $client->responseCode() . "\n";
 foreach ( $client->responseHeaders() ) {
   print 'Header: ' . $_ . '=' . $client->responseHeader($_) . "\n";
 }
 
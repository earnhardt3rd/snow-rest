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
my $request_body ="{\"sys_tags\":\"\"}";
 
 my $client = REST::Client->new(host => $host);
 
 my $encoded_auth = encode_base64("$user:$pwd", '');
 
 $client->POST("/api/now/table/u_zsource",
                $request_body,
                {'Authorization' => "Basic $encoded_auth",
                 'Content-Type' => 'application/json',
                 'Accept' => 'application/json'}); 
 
 print 'Response: ' . $client->responseContent() . "\n";
 print 'Response status: ' . $client->responseCode() . "\n";
 foreach ( $client->responseHeaders() ) {
   print 'Header: ' . $_ . '=' . $client->responseHeader($_) . "\n";
 }
 
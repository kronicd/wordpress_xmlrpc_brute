# Wordpress XML RPC brute force thingy

Script was created during an engagement where the wp-login had been deleted and wordfence prevented the traditional approach of sending thousands of attempts in a single API call.

The tool takes a list of usernames and passwords, then iterates through them one at a time, against an xml-rpc endpoint.

## Deps
    wordpress_xmlrpc python lib
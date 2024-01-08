# 0x0F. Load balancer

0. 0-custom_http_response_header: Configure web-02 to be identical to web-01
1. 1-install_load_balancer: Install and configure HAproxy on your lb-01 server
2. 2-puppet_custom_http_response_header.pp: Add a custom HTTP header with Puppet
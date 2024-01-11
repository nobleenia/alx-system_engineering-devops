# 0x10. HTTPS SSL

0. 0-world_wide_web: Configure the domain zone so that the subdomain www points to your load-balancer IP (lb-01)
1. 1-haproxy_ssl_termination: Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www
# Puppet Manifest to Adjust Nginx ULIMIT and Restart Nginx Service
# The first exec resource is tasked with modifying the Nginx configuration
# to adjust the ULIMIT setting, which controls the maximum open files.
# Puppet file to replace a line...

exec {'fix--for-nginx':
  command  =>  '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  path     =>  '/usr/local/bin/:/bin/'
}

# The second exec resource is responsible for restarting the Nginx service.
# This is necessary to apply the changes made to the ULIMIT setting.
# Restart nginx
exec {'nginx-restart':
  command =>  '/etc/init.d/nginx restart',
  path    =>  '/etc/init.d'
}
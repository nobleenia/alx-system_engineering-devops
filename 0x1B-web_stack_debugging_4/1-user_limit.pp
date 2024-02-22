#Puppet resource to increase file open limit

exec {'sed replace':
  command  =>  'sed -i "s/^holberton hard.*/holberton hard nofile 2048/" /etc/security/limits.conf',
  path     =>  '/bin',
  provider =>   'shell',
}

exec {'sed replacement':
  command  => 'sed -i "s/^holberton soft.*/holberton soft nofile 1024/" /etc/security/limits.conf',
  path     =>  '/bin',
  provider =>   'shell',
}
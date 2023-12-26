# Install flask using puppet

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}

package { 'werkzeug':
  ensure   => '2.0.2',  # Specify a version compatible with Flask 2.1.0
  provider => 'pip3',
}
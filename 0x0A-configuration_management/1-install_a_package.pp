# Puppet manifest to install Flask using a virtual environment
package { 'python3-venv':
  ensure => present,
}

exec { 'create_virtualenv':
  command => '/usr/bin/python3 -m venv /path/to/venv',
  path    => ['/usr/bin'],
  creates => '/path/to/venv',
  require => Package['python3-venv'],
}

exec { 'install_flask_in_virtualenv':
  command => '/path/to/venv/bin/pip3 install Flask==2.1.0',
  path    => ['/path/to/venv/bin'],
  creates => '/path/to/venv/lib/python3.11/site-packages/flask',
  require => Exec['create_virtualenv'],
}

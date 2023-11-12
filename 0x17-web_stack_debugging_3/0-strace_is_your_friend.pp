file { '/etc/apache2/apache2.conf':
  ensure  => 'present',
  content => '
    DefaultRuntimeDir /var/run/apache2
  ',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
}

file { '/etc/apache2/apache2.conf':
  ensure  => 'present',
  content => '
    DefaultRuntimeDir /var/run/apache2
  ',
  notify  => Service['apache2'],
}

file { '/etc/apache2/mods-available/mpm_prefork.conf':
  ensure  => 'present',
  content => '
    <IfModule mpm_prefork_module>
        StartServers             5
        MinSpareServers          5
        MaxSpareServers          10
        MaxClients              150
        MaxRequestsPerChild     0
    </IfModule>
  ',
  notify  => Service['apache2'],
}

file { '/etc/apache2/mods-enabled/mpm.conf':
  ensure => 'link',
  target => '/etc/apache2/mods-available/mpm_prefork.conf',
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
}

notify { 'Debug Message':
  message => "Puppet ran successfully up to this point.",
}

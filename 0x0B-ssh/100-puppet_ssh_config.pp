# Ensure SSH client configuration file
file { '/etc/ssh/ssh_config':
  ensure => present,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
}

# Include the puppetlabs/stdlib module
include stdlib

# Configure SSH client
stdlib::file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  require => File['/etc/ssh/ssh_config'],
}

stdlib::file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  require => File['/etc/ssh/ssh_config'],
}

# Notify that changes have been made
notify { 'SSH client configuration updated':
  require => [Stdlib::File_line['Declare identity file'], Stdlib::File_line['Turn off passwd auth']],
}

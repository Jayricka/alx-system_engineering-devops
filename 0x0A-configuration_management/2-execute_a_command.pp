exec { 'kill_killmenow':
  command     => 'sudo pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

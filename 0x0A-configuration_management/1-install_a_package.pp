# Puppet manifest to install Flask system-wide
package { 'python3-flask':
  ensure => '2.2.2-2ubuntu1.1',
}

# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Configure Nginx for port 80
file { '/etc/nginx/sites-available/default':
  ensure => file,
  content => "
server {
  listen 80;
  root /var/www/html;
  index index.html;

  location / {
    return 200 'Hello World!';
  }

  location /redirect_me {
    return 301 'https://www.linkedin.com/in/rikagachanja/';
  }
}
  ",
  notify => Service['nginx'],
}

# Create a symlink to enable the site
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Remove the default Nginx configuration
file { '/etc/nginx/sites-enabled/default':
  ensure => absent,
  notify => Service['nginx'],
}

# Ensure Nginx service is running and enabled
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/etc/nginx/sites-enabled/default'],
}


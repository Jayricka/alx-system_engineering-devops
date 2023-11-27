# 7-puppet_install_nginx_web_server.pp

# Install Nginx package
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx service is running
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Create a basic HTML file with Hello World content
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx to listen on port 80
file { '/etc/nginx/sites-available/default':
  ensure => present,
  content => "server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
",
  notify => Service['nginx'],
}

# Restart Nginx when the configuration changes
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  refreshonly => true,
  subscribe   => File['/etc/nginx/sites-available/default'],
}

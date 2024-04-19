#!/usr/bin/puppet
# Let's manifest Puppet to install Flask from pip3

package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  creates => '/usr/local/lib/python3.8/dist-packages/Flask',
  path    => ['/usr/bin'],
}


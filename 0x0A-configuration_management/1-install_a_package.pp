#!/usr/bin/puppet
# Let's manifest Puppet to install Flask from pip3
package {'flask':
	ensure	 => '2.1.0',
	provider => 'pip'
}

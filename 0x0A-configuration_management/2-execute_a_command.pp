# Puppet manifest to kill a process named killmenow
exec { 'pkill killmenow':
  path => '/usr/bin:/usr/abin:/bin',
}


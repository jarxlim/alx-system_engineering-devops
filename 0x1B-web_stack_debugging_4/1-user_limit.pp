exec { 'increase-hard-file-limit':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/hard nofile [0-9]\+/hard nofile 97816/g'"
}

exec { 'increase-soft-file-limit`':
  command => "/bin/sed -i /etc/security/limits.conf -e 's/soft nofile [0-9]\+/soft nofile 97816/g'"
}

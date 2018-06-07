file { '/tmp/file.txt':
  ensure => file,
  content => 'my first file'
}

from distutils.core import setup

pkg = 'Remote channel stream converter'
setup (name = 'enigma2-plugin-extensions-remotestreamconverter',
	version = '1.0',
	description = 'Convert remote channel list for streaming',
	packages = [pkg],
	package_dir = {pkg: 'plugin'}
)

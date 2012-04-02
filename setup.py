from distutils.core import setup

pkg = 'Extensions.RemoteChannelStreamConverter'
setup (name = 'enigma2-plugin-extensions-remotechannelstreamconverter',
	version = '1.0',
	description = 'Convert remote channel list for streaming',
	packages = [pkg],
	package_dir = {pkg: 'plugin'}
)

from distutils.core import setup

pkg = 'RemoteChannelStreamConverter'
setup (name = 'enigma2-plugin-systemplugins-remote-channel-stream-converter',
	version = '1.0',
	description = 'Convert remote channel list for streaming',
	packages = [pkg],
	package_dir = {pkg: 'plugin'}
)

from distutils.core import setup
import setup_translate

pkg = 'Extensions.RemoteChannelStreamConverter'
setup(name='enigma2-plugin-extensions-remotechannelstreamconverter',
	version='1.0',
	description='Convert remote channel list for streaming',
	packages=[pkg],
	package_dir={pkg: 'plugin'},
	package_data={pkg: ['locale/*/LC_MESSAGES/*.mo']},
	cmdclass=setup_translate.cmdclass, # for translation
)

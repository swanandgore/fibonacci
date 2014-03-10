from distutils.core import setup
setup(
	name='fibonacci',
	version='1.0',
	py_modules=['fibonacci'],
	packages=['fibonacci'],
	package_dir={'fibonacci': 'src/fibonacci'},
)


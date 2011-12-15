
try:
    from setuptools import setup
except ImportError:
    print "Falling back to distutils. Functionality may be limited."
    from distutils.core import setup

config = {
    'description'       : 'A implementation of tee in Python',
    'author'            : 'Brandon Sandrowicz',
    'url'               : 'http://github.com/bsandrow/pytee',
    'author_email'      : 'brandon@sandrowicz.org',
    'version'           : 0.1,
    'py_modules'        : ['pytee'],
    'name'              : 'pytee',
}

setup(**config)

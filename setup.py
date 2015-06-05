try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
import mailgun3

setup(
    name=mailgun3.__title__,
    packages=[mailgun3.__title__],
    version=mailgun3.__version__,
    description='A python client for Mailgun API v3',
    long_description=open('README.md', 'rt').read(),
    author=mailgun3.__author__,
    author_email='fatisar@gmail.com',
    url='https://github.com/fatisar/python-mailgun3',
    download_url="https://github.com/fatisar/python-mailgun3/archive/%s.tar.gz" % mailgun3.__version__,
    keywords=['mailgun', 'email'],
    install_requires=[
        'requests>=2.6.0',
    ],
    test_suite="tests",
    tests_require=[
        'mock>=0.8',
    ],
)

import ast
import os

from setuptools import setup, find_packages


def get_version():
    path = os.path.join(os.path.dirname(__file__), 'threema/gateway/__init__.py')
    with open(path) as file:
        for line in file:
            if line.startswith('__version__'):
                _, value = line.split('=', maxsplit=1)
                return ast.literal_eval(value.strip())

# Allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
# Import long description
long_description = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

setup(
    name='threema.gateway',
    version=get_version(),
    packages=find_packages(),
    namespace_packages=['threema'],
    install_requires=[
        'py_lru_cache>=0.1.4,<0.2',
        'logbook>=1,<2',
        'libnacl>=1.4,<1.5',
        'click>=5.1,<6',
        'aiohttp>=1,<2',
        'asyncio>=3.4.3,<3.5',
    ],
    tests_require=[
        'pytest>=2.8.4',
        'pytest-asyncio>=0.2.0',
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'threema-gateway = threema.gateway.bin.gateway_client:main',
            'threema-callback-server = threema.gateway.bin.callback_server:main',
        ],
    },

    # PyPI metadata
    author='Lennart Grahl',
    author_email='lennart.grahl@threema.ch',
    description=('An API for the Threema gateway service to send and receive'
                 'messages including text, images, files and delivery reports.'),
    long_description=long_description,
    license='MIT License',
    keywords='threema gateway service sdk api',
    url='https://gateway.threema.ch/',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Security',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
    ],
)

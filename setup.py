from os import path

from setuptools import setup

BASE_DIR = path.abspath(path.dirname(__file__))
with open(path.join(BASE_DIR, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


# based on https://packaging.python.org/guides/single-sourcing-package-version/
def get_version():
    version_file = path.join(BASE_DIR, 'csc_dummy', 'version.py')
    with open(version_file, encoding='utf-8') as f:
        for line in f:
            if line.startswith('__version__'):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        raise RuntimeError("Unable to find version string.")


setup(
    name='certomancer-csc-dummy',
    version=get_version(),
    packages=['csc_dummy'],
    url='https://github.com/MatthiasValvekens/certomancer-csc-dummy',
    license='MIT',
    author='Matthias Valvekens',
    author_email='dev@mvalvekens.be',
    description='A Certomancer-based demo CSC server for integration tests',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',

        'Topic :: Security :: Cryptography',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    entry_points={
        "console_scripts": [
            "certomancer-csc = csc_dummy.__main__:launch"
        ]
    },
    install_requires=[
        'asn1crypto>=1.5.0',
        'cryptography>=3.3.1',
        'certomancer >=0.8.3, <0.10.0',
        'aiohttp~=3.8.0',
        'python-pae==0.1.0',
    ],
    setup_requires=['wheel',],
    keywords="pki testing csc signature"
)

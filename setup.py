# encoding: utf-8
from setuptools import setup, find_packages

setup(
    name = 'dokku-controller-agent',
    version = '0.1',
    description = '',
    author = u'Kristian Øllegaard',
    author_email = 'kristian@kristian.io',
    zip_safe=False,
    include_package_data = True,
    packages = find_packages(exclude=[]),
    py_modules=['agent'],
    install_requires=[
        open("requirements.txt").readlines(),
    ],
)

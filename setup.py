# -*- coding: utf-8 -*-
import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='b2fuse',
    version=1.3,
    description="FUSE integration for Backblaze B2 Cloud storage",
    long_description=read('README.md'),
    classifiers=[
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5  ',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8'
    ],
    keywords='',
    author='Sondre Engebraaten',
    packages=find_packages(),
    install_requires=['b2==1.4.2', 'fusepy==3.0.1', 'PyYAML==5.3'],
    include_package_data=True,
    zip_safe=True,
    entry_points={
        'console_scripts': ['b2fuse = b2fuse.b2fuse:main',],
    }
)

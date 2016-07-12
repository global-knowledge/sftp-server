#!/usr/bin/env python
import os
from distutils.core import setup


classifiers = """\
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Programming Language :: Python
Topic :: Internet :: File Transfer Protocol (FTP)
Operating System :: Unix, Linux, Windows, Mac
"""

def read(*rel_names):
    return open(os.path.join(os.path.dirname(__file__), *rel_names)).read()


setup(
    name='sftpserver',
    version='0.3',
    url='http://github.com/global-knowledge/sftp-server',
    license='MIT',
    install_requires=['paramiko'],
    packages=['src'],
    zip_safe=False,
    entry_points="""\
    [console_scripts]
    sftpserver = sftpserver:main
    """,
    classifiers=filter(None, classifiers.split('\n')),
    description='sftp-server - a simple single-threaded sftp server',
    long_description=read('README'),
    )

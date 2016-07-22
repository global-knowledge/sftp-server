from distutils.core import setup


setup(
    name='sftp_server',
    packages=['sftp_server'],
    package_data={
        'sftp_server': ['credentials.json'],
    },
    version='0.3',
    description='sftp_server - a simple single-threaded sftp server',
    author='Ruslan Spivak',
    author_email='ruslan.spivak@gmail.com',
    url='https://github.com/global-knowledge/sftp-server',
    license='MIT License',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'sftp_server = sftp_server:main',
        ],
    },
    keywords=['sftp', 'ssh', 'server'],
    classifiers=[],
    install_requires=['paramiko'],
)

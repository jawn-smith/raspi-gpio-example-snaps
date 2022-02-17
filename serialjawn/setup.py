from setuptools import setup

setup(
    name='Serial Jawn',
    version='1.0',
    description='Send and receive messages over uart',
    author='jawn-smith',
    py_modules=['serialjawn'],
    entry_points = {
        'console_scripts': ['serialjawn=serialjawn:main'],
    }
)

from setuptools import setup

setup(
    name='I2C Jawn',
    version='1.0',
    description='Blink an LED until ctrl+C is detected',
    author='jawn-smith',
    py_modules=['i2cjawn'],
    entry_points = {
        'console_scripts': ['i2cjawn=i2cjawn:main'],
    }
)

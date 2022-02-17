from setuptools import setup

setup(
    name='GPIO Jawn',
    version='1.0',
    description='Blink an LED until ctrl+C is detected',
    author='jawn-smith',
    py_modules=['gpiojawn'],
    entry_points = {
        'console_scripts': ['gpiojawn=gpiojawn:main'],
    }
)

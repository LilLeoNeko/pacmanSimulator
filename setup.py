from setuptools import setup
setup(
    name = 'cmdline-pacman',
    version = '1.0.0',
    packages = ['pacmanSimulator'],
    entry_points = {
        'console_scripts': [
            'pacmanSimulator = pacmanSimulator.__main__:startGame'
        ]
    })
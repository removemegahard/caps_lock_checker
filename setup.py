from setuptools import setup, find_packages

setup(
    name='caps_lock_checker',
    version='1.0',
    description='A simple Caps Lock status checker application using Tkinter',
    author='RemoveMegahard',
    author_email='removemegahard@outlook.com',
    packages=find_packages(),
    install_requires=[
        'keyboard==0.13.5',
    ],
    entry_points={
        'console_scripts': [
            'caps_lock_checker=caps_lock_checker:main',
        ],
    },
)

import os
from setuptools import setup

setup(
    name="Jeev-Modules",
    version='0.0.1',
    author="Jacob Heinz",
    author_email="me@jh.gg",
    description="Modules for Jeev",
    license="MIT",
    keywords="chat slack bot irc jeev",
    url="https://github.com/jhgg/jeev",
    packages=['modules'],
    package_dir = {'jeev.modules':'jeev'},
    install_requires=[
        'jeev',
    ],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Communications :: Chat",
        "Topic :: Utilities",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 2 :: Only",
        "License :: OSI Approved :: MIT License",
    ],
)
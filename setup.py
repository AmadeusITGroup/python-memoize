#!/usr/bin/env python
"""
memoize
--------------

**memoize** is an implementation
of `memoization <http://en.wikipedia.org/wiki/Memoization>` with persistent storage using redis.
. You can think of it as a cache for function or method results.

"""

from setuptools import setup

setup(
    name="python-memoize",
    version="1.0.0",
    packages=["memoize"],
    tests_require = [
        'pytest',
        'mock',
        'fakeredis',
        'freezegun'
    ],
    include_package_data=True,
    license="BSD License",
    description="An implementation of memoization technique (not django-specific).",
    url="https://github.com/AmadeusITGroup/python-memoize",
    long_description=__doc__,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)

#!/usr/bin/env python
"""
microinvoices
=====

"""

import microinvoices
from setuptools import setup, find_packages
import sys

install_requires = [
    "Django==1.8.2",
    "raven==5.2.0",
]

dev_requires = [
    'django-debug-toolbar',
]

test_requires = [
    "pytest",
    "pytest-cov",
    "pytest-django",
]


setup(
    name="microinvoices",
    version=microinvoices.__version__,
    author="Xavier Ordoquy",
    author_email="xordoquy@linovia.com",
    url="",
    description="Webservice / microservice for invoices",

    # Packages and data to take into account
    packages=find_packages(exclude=("tests", "tests.*")),
    include_package_data=True,

    zip_safe=False,  # Avoid eggs

    # Allow pip install .[tests,dev] to install the dev and test dependencies
    extras_require={
        "tests": test_requires,
        "dev": dev_requires,
    },
    install_requires=install_requires,
    tests_require=test_requires,
)

import os
import setuptools
from snowflakeclient.version import get_version

readme = open('README.md').read()

long_description = """
python-snowflakeclient %s
Another python snowflake client. This one works, it's current and
is part of iPlantCollaborative's infrastructure.

To install use pip install git+git://github.com/jmatt/python-snowflakeclient

----

%s

----

For more information, please see: https://github.com/jmatt/python-snowflakeclient
""" % (get_version('short'), readme)

setuptools.setup(
    name='python-snowflakeclient',
    version=get_version('short'),
    author='jmatt',
    author_email='jmatt@jmatt.org',
    description="Console script and python client library for twitter's Snowflake service.",
    long_description=long_description,
    license="Apache License, Version 2.0",
    url="https://github.com/jmatt/python-snowflakeclient",
    packages=setuptools.find_packages(),
    install_requires=['thrift>=0.9'],
    include_package_data=True,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Java",
        "Topic :: Software Development :: Libraries",
        "Topic :: System :: Distributed Computing"
    ],
    entry_points={
        "console_scripts": ["snowflake.py = snowflakeclient.snowflake:main"]
    }
)

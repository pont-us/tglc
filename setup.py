"""Setup script for tglc"""

import os.path
from setuptools import setup

cwd = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(cwd, "README.adoc")) as fh:
    long_desc = fh.read()

setup(
    name="tglc",
    version="1.0.0",
    author="Pontus Lurcock",
    author_email="pont@talvi.net",
    description="Manipulate 2G magnetometer data files.",
    long_description=long_desc,
    long_description_content_type="text/asciidoc",
    url="https://github.com/pont-us/tglc",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["tglc"],
)

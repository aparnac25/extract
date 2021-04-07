#!/usr/bin/env python
"""
Install extract package. To install locally use: pip install -e .
"""

from setuptools import setup

# build command
setup(
    name="extract",
    version="0.0.2",
    author="Aparna Chandrashekar",
    author_email="achandrashekar@gradcenter.cuny.edu",
    description="program to read PDF and extract coordinates to plot onto map'",
    install_requires = ["pandas", "tika", "folium"], 
    classifiers=["Programming Language :: Python :: 3"],
    scripts= ['extract/extract.py']
)
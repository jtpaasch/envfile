# -*- coding: utf-8 -*-

"""The ``setup.py`` file for ``envfile``."""

from setuptools import setup, find_packages
from codecs import open
from os import path


# Where are we? Full path.
here = path.abspath(path.dirname(__file__))

# Get the long description from the README file.
with open(path.join(here, "README.rst"), encoding="utf-8") as f:
    long_description = f.read()

setup(

    # What's the project's name?
    # E.g., when you type ``pip install <name>``.
    name="envfile",

    # Version should comply with PEP440.
    version="0.1.0",

    # Describe the project.
    description="Loads/unloads environment variables from a .env file.",
    long_description=long_description,
    keywords="environment variables",

    # The project's main homepage.
    url="https://github.com/jtpaasch/envfile",

    # Author details.
    author="JT Paasch",
    author_email="jt.paasch@gmail.com",

    # Choose a license.
    license="MIT",

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[

        # How mature is the project?
        "Development Status :: 3 - Alpha",

        # Who and what is it for?
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",

        # What's the license (should match the ``license`` param above).
        "License :: OSI Approved :: MIT License",

        # Which languages/versions does this work with?
        "Programming Language :: Python :: 3.4",

    ],

    # Which packages should be included in the dist?
    packages=find_packages(
        exclude=[
            "venv",
            "tests",
        ]
    ),

    # What are the run-time dependencies?
    # Pip will install these when you install this package.
    install_requires=["click"],

    # Are there any extra dependency groups, e.g., for testing?
    extras_require={
        "test": [
            "coverage",
            "flake8",
            "pep257",
        ],
    },

    # This is an executable script, so where is/are the entry point/s?
    entry_points={
        "console_scripts": [
            "envfile = envfile.application:main",
        ],
    },

)

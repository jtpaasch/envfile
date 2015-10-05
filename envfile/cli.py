# -*- coding: utf-8 -*-

"""The ``cli`` module for the ``envfile`` package.

This module contains the main entrypoint into the application.
The ``envfile`` program can be accessed through ``main()``.

"""

from os import environ

# The ``click`` package is for building command line tools.
import click

# For parsing each line of a .env file.
from envfile.parse import parse

# Click's default help option is just ``--help``.
# We want both ``-h`` and ``--help`` to work.
# We'll modify the context settings to do that.
CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument("filepath", type=click.File("r"))
@click.option(
    "-u",
    "--unload",
    is_flag=True,
    default=False,
    help="Unload the variables in FILEPATH."
)
def cli(filepath, unload=False, parse=parse):
    """Load variables from FILEPATH into the environment."""
    for line in filepath:

        # Get the key and value from each line.
        key, value = parse(line)
        if key is not None and value is not None:

            # Load (or unload) the environment variable.
            if unload:
                del environ[key]
            else:
                environ[key] = value

            # Output what the key/value pair is.
            # This is important, because the user might
            # want to pipe the output into a file or something.
            output = key + "=" + value
            click.echo(output)

# -*- coding: utf-8 -*-

"""The ``parse`` module for the ``envfile`` package.

This module contains tools that can parse lines in envfiles,
i.e., files with KEY=value declarations, one per line.

"""


def parse(line):
    """Get the key/value pair out of the text ``KEY=value``.

    This function will ignore the following:

    * Commented lines (lines that begin with #).
    * Lines that have no equals sign in them.

    """
    key = None
    value = None
    if not line.startswith("#"):
        parts = line.split("=", maxsplit=1)
        if len(parts) == 2:
            key = parts[0].strip()
            value = parts[1].strip()
    return (key, value)

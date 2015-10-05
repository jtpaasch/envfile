# -*- coding: utf-8 -*-

"""Tests properties of the ``parse`` module."""

from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import text

from envfile.parse import parse

class TestAddition(TestCase):

    @given(text())
    def test_parse_only_parses_lines_with_equals_sign(self, sample):
        """Ensure ``parse()`` only parses lines containing an equals sign.

        Without an equal sign, the ``parse()`` function obviously cannot
        extract a key from one side and a value from the other side of it.
        Only lines with an equal sign should return a (key, value) pair
        of the form (<string>, <string>), even if either <string> is empty.

        """
        key, value = parse(sample)
        if "=" in sample:
            assert key is not None and value is not None
        else:
            assert not key and not value
                

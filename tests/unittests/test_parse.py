# -*- coding: utf-8 -*-

"""Unit tests for the ``parse`` module."""

from unittest import TestCase

from envfile.parse import parse


class TestParse(TestCase):

    """Unit tests for the ``parse`` module."""
    
    def test_parse_trims_keys_and_values(self):
        """Test that ``parse()`` trims the key and value.

        The ``parse()`` function should trim the key and value it extracts.

        """
        key, value = parse("This = that")
        assert (key, value) == ("This", "that")
    
    def test_parse_ignores_comments(self):
        """Test ``parse()`` ignores comments.

        The ``parse()`` function should return no key and value
        for a comment line (i.e., a line that begins with a #).

        """
        key, value = parse("# This line is a comment.")
        assert (key, value) == (None, None)

    def test_parse_ignores_lines_sans_equals_signs(self):
        """Test ``parse()`` ignores lines without equals signs.

        The ``parse()`` function should return no key and value
        for a line without any equal signs.

        """
        key, value = parse("This line has no equals sign in it.")
        assert (key, value) == (None, None)

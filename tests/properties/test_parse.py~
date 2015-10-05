# -*- coding: utf-8 -*-

"""Property tests."""

from unittest import TestCase
from hypothesis import given
from hypothesis.strategies import integers


class TestAddition(TestCase):

    @given(integers(), integers())
    def test_int_addition_is_commutative(self, x, y):
        assert x + y == y + x

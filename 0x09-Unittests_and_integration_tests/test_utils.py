#!/usr/bin/env python3
"""
access_nested_map Test Module
0x09. Unittests and Integration Tests
holbertonschool-web_back_end
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """[TestAccessNestedMap]

    Args:
        unittest ([UnitTestClass]): [Base class]
    """

    @parameterized.expand([
        ("map1", {"a": 1}, ("a",), 1),
        ("map2", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("map3", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """[summary]

        Args:
            name ([type]): [description]
            nested_map ([type]): [description]
            path ([type]): [description]
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

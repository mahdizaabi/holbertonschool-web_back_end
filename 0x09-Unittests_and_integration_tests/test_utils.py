#!/usr/bin/env python3
"""
access_nested_map Test Module
0x09. Unittests and Integration Tests
holbertonschool-web_back_end
"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

from unittest.mock import patch
from unittest.mock import Mock, PropertyMock, MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """[TestAccessNestedMap testing class subclassed from unittest.TestCase]

    Args:
        unittest ([UnitTestClass]): [Base class]
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map: Mapping,
                               path: Sequence, expected: Any) -> bool:
        """[summary]

        Args:
            nested_map ([Mapping]): [nested mapping]
            path ([sequence]): []
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([({}, ("a"), KeyError), ({"a": 1},
                                                   ("a", "b"), KeyError)])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """[test method:assertRaises context manager
        to test that a KeyError is raised]

        Args:
            nested_map ([mapping]): [description]
            path ([Squence]): [description]
            expected ([KeyError]): [description]
        """
        with self.assertRaises(KeyError) as raises:
            access_nested_map(nested_map, path)
            self.assertEqual(raises.exception.message, KeyError)


class TestGetJson(unittest.TestCase):
    """[summary]

    Args:
        unittest ([type]): [description]
    """

    def response(self, payload):
        """[summary]
        """
        response_mock = Mock()
        response_mock.json.return_value = payload
        return response_mock

    @parameterized.expand([("http://example.com", {"payload": True},
                            {"payload": True}),
                           ("http://holberton.io", {"payload": False},
                            {"payload": False})])
    def test_get_json(self, url, payload, expected):
        """[summary]
        """
        with patch('utils.requests') as mock_requests:
            mock_requests.get.return_value = self.response(payload)
            self.assertEqual(get_json(url), expected)
            assert mock_requests.get.call_count == 1


class TestMemoize(unittest.TestCase):
    """[summary]
    Args:
    unittest ([type]): [description]
    """

    def test_memoize(self):
        """[summary]"""
        class TestClass:
            """[summary]"""

            def a_method(self):
                """[summary]"""
                return 42

            @memoize
            def a_property(self):
                """[summary]"""
                return self.a_method()

        c = TestClass()
        c.a_method = MagicMock(return_value=42)
        self.assertEqual(c.a_property, 42)
        self.assertEqual(c.a_property, 42)
        c.a_method.assert_called_once()

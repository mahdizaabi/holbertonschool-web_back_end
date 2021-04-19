#!/usr/bin/env python3
"""
test_client.py
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
from fixtures import TEST_PAYLOAD
from client import GitHubOrgClient


class TestGitHubOrgClient(unittest.TestCase):
    """[TestGitHubOrgClient]

    Args:
        unittest ([unittest Class]): [Unit test Base class]
    """

    @parameterized.expand([('google', TEST_PAYLOAD), ('abc', {})])
    def test_org(self, org, expected):
        """[testing the GitHubOrgClient.org module]
        """

        instance = GitHubOrgClient(org)

        with patch('client.get_json') as mock_requests:
            instance = GitHubOrgClient(org)
            mock_requests.return_value = expected
            self.assertEqual(instance.org, expected)
            self.assertEqual(instance.org, expected)
            mock_requests.assert_called_once_with(
                'https://api.github.com/orgs/google')

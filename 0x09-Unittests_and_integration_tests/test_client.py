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

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(input)
        test_class.org()
        mock.assert_called_once_with(f'https://api.github.com/orgs/{input}')

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org, mock_requests):
        """[testing the GitHubOrgClient.org module]
        """
        instance = GitHubOrgClient(org)
        mock_requests.side_effect = Exception()
        try:
            instance.org()
        except Exception as e:
            mock_requests.assert_called_once_with(
                "https://api.github.com/orgs/{}".format(org))
            pass

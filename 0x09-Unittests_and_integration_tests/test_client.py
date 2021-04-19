#!/usr/bin/env python3
"""
test_client.py
0x09. Unittests and Integration Tests
holbertonschool-web_back_end
"""
import unittest
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

from unittest.mock import patch
from unittest.mock import Mock, PropertyMock
from fixtures import TEST_PAYLOAD
from client import GitHubOrgClient


class TestGitHubOrgClient(unittest.TestCase):
    """[TestGitHubOrgClient]

    Args:
        unittest ([unittest Class]): [Unit test Base class]
    """

    @parameterized.expand([('google'), ('abc')])
    @patch('client.get_json')
    def test_org(self, org, mock_requests):
        """[testing the GitHubOrgClient.org module]
        """
        instance = GitHubOrgClient(org)
        instance.org()
        mock_requests.assert_called_once_with(
            f'https://api.github.com/orgs/{org}')

    @parameterized.expand([('google', TEST_PAYLOAD[0][0])])
    def test_public_repos_url(self, org, expected):
        """[testing the public methode]
        """
        with patch('client.GitHubOrgClient') as mock_requests:
            instance = GitHubOrgClient(org)
            mock_requests.org.return_value = expected
            self.assertEqual(instance._public_repos_url, expected['repos_url'])

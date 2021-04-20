#!/usr/bin/env python3
""" Module for testing client """

from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from parameterized import parameterized, parameterized_class
import json
import unittest
from unittest.mock import patch, PropertyMock, Mock


class TestGithubOrgClient(unittest.TestCase):
    """ Github org Testing class """

    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, input, mock):
        """testing class method org"""
        test_class = GithubOrgClient(input)
        mock.side_effect = Exception()
        try:
            test_class.org()
        except Exception as e:
            mock.assert_called_once_with(
                f'https://api.github.com/orgs/{input}')

    @parameterized.expand([('google', TEST_PAYLOAD[0][0])])
    def test_public_repos_url(self, org, expected):
        """ Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch('client.GithubOrgClient') as mock:
            instance = GithubOrgClient(org)
            mock.org.return_value = expected
            self.assertEqual(instance._public_repos_url, expected["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, jsmock):
        """[test the result of fetching all PUBLIC Repository containing
            specific licence, or None otherwise]
        """
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as propertyMock:
            propertyMock.return_value = 'return from property'
            jsmock.return_value = [{'name': 'repo'}]
            instance = GithubOrgClient('fakeUrl')
            expected = ['repo']
            result = instance.public_repos()
            propertyMock.assert_called_once()
            jsmock.assert_called_once()

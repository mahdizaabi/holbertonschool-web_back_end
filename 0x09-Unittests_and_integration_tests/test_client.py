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
    def test_public_repos(self, mock_json):
        """[test the result of fetching all PUBLIC Repository containing
            specific licence]
        """

        Response_payload = [{"name": "Google"}]
        mock_json.return_value = Response_payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            result = test_class.public_repos()

            check = [rep["name"] for rep in Response_payload]
            self.assertEqual(result, check)

            mock_public.assert_called_once()
            mock_json.assert_called_once()

    @parameterized.expand([({"license": {"key": "my_license"}}, "my_license", True),
                           ({"license": {"key": "other_license"}}, "my_license", False)])
    def test_has_license(self, mapping, license_key, excepted):
        """[test test_has_license]
        """

        self.assertEqual(GithubOrgClient.has_license(mapping, license_key), excepted)

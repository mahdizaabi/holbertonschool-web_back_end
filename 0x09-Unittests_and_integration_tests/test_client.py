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
        with patch('client.get_json') as mock:
            instance = GithubOrgClient(org)
            mock.return_value = expected
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

        self.assertEqual(GithubOrgClient.has_license(
            mapping, license_key), excepted)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ example payloads found example payloads found  """
    @classmethod
    def setUpClass(cls):
        """  unittest.TestCase
        method to return example payloads found in the fixtures """
        cls.get_patcher = patch('requests.get')
        cls.mock = cls.get_patcher.start()
        cls.mock.return_value.json.side_effect = [
            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,
        ]

    def test_public_repos(self):
        """[implement the test_public_repos method to test
        GithubOrgClient.public_repos.]
        """

        test_class = GithubOrgClient('do')
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class._public_repos_url,
                         self.org_payload["repos_url"])
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """[Implement test_public_repos_with_license to test the public_repos with the argument license="apache-2.0"
            and make sure the result matches the expected value from the fixtures.]
        """
        test_class = GithubOrgClient("google")
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("nolicence"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """the unittest.TestCase API
        mexample payloads found example payloads found  """
        cls.get_patcher.stop()

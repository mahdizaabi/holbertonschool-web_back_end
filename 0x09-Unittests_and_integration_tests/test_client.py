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
from test_client import GitHubOrgClient


class TestGitHubOrgClient(unittest.TestCase):
    """[TestGitHubOrgClient]

    Args:
        unittest ([unittest Class]): [Unit test Base class]
    """

    def test_org(cls):
        """[testing the GitHubOrgClient.org module]
        """

#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
from client import GithubOrgClient


@parameterized_class([
    {"org_name": "google"},
    {"org_name": "abc"},
])
class TestGithubOrgClient(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Patch requests.get for all tests in this class
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        cls.get_patcher.stop()

    def test_org(self):
        """Test org method returns correct data"""
        expected = {"login": self.org_name}
        self.mock_get.return_value.json.return_value = expected
        client = GithubOrgClient(self.org_name)
        self.assertEqual(client.org(), expected)
        self.mock_get.assert_called_once()

    def test_public_repos(self):
        """Test public_repos returns list of repo names"""
        repos_data = [
            {"name": "repo1"},
            {"name": "repo2"},
        ]
        self.mock_get.return_value.json.return_value = repos_data
        client = GithubOrgClient(self.org_name)
        result = client.public_repos()
        self.assertEqual(result, ["repo1", "repo2"])

    def test_public_repos_with_license(self):
        """Test public_repos filters repos by license"""
        repos_data = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": None},
        ]
        self.mock_get.return_value.json.return_value = repos_data
        client = GithubOrgClient(self.org_name)
        result = client.public_repos(license="mit")
        self.assertIn("repo1", result)
        self.assertNotIn("repo2", result)
        self.assertNotIn("repo3", result)

    def test_has_license(self):
        """Test has_license static method"""
        repo = {"license": {"key": "mit"}}
        self.assertTrue(GithubOrgClient.has_license(repo, "mit"))
        self.assertFalse(GithubOrgClient.has_license(repo, "apache-2.0"))
        self.assertFalse(GithubOrgClient.has_license({"license": None}, "mit"))
        self.assertFalse(GithubOrgClient.has_license({}, "mit"))


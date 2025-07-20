#!/usr/bin/env python3
"""
GithubOrgClient module
"""
from typing import List
import requests


class GithubOrgClient:
    """GithubOrgClient class"""

    ORG_URL = "https://api.github.com/orgs/{org}"

    def __init__(self, org: str) -> None:
        """Initialize with organization name"""
        self.org_name = org

    def org(self) -> dict:
        """Get organization information"""
        url = self.ORG_URL.format(org=self.org_name)
        return self.get_json(url)

    @staticmethod
    def get_json(url: str) -> dict:
        """Fetch JSON data from a URL"""
        response = requests.get(url)
        return response.json()

    @property
    def _public_repos_url(self) -> str:
        """Return the URL for the list of public repos"""
        return self.org().get("repos_url")

    def public_repos(self, license: str = None) -> List[str]:
        """Return a list of public repos (filtered by license if given)"""
        repos = self.get_json(self._public_repos_url)
        if license is None:
            return [repo["name"] for repo in repos]
        return [
            repo["name"]
            for repo in repos
            if self.has_license(repo, license)
        ]

    @staticmethod
    def has_license(repo: dict, license_key: str) -> bool:
        """Check if repo has a specific license"""
        license_info = repo.get("license")
        return license_info is not None and license_info.get("key") == license_key

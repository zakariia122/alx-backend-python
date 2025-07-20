#!/usr/bin/env python3
"""
Unit tests for client.py
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import client

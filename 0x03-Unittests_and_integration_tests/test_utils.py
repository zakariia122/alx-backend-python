#!/usr/bin/env python3
"""
Unittest for utils functions
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, memoize
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map returns expected result"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand(
        [
             ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError), 
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """Test access_nested_map raises correct exception"""
        with self.assertRaises(expected_exception):
            access_nested_map(nested_map, path)


class TestMemoize(unittest.TestCase):
    """Test class for memoize"""

    def test_memoize(self):
        """Test memoize decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method", return_value=42) as mock_method:
            test_obj = TestClass()
            result_1 = test_obj.a_property
            result_2 = test_obj.a_property

            mock_method.assert_called_once()
            self.assertEqual(result_1, 42)
            self.assertEqual(result_2, 42)

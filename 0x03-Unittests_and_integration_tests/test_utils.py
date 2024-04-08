#!/usr/bin/env python3
"""
Shebang to create a PY script
"""


import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, MagicMock


access_nested_map = __import__('utils').access_nested_map
get_json = __import__('utils').get_json
memoize = __import__('utils').memoize


class TestAccessNestedMap(unittest.TestCase):
    """class to test AccessNestedMap"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """method to test access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "Key 'a' not found in nested map"),
        ({"a": 1}, ("a", "b"), "Key 'b' not found in nested map['a']"),
        ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_message):
        """method to test exception raised"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """class to test get_json method from utils.py"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """method to test get_json using mock"""
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        result = get_json(test_url)

        mock_get.assert_called_once_with(test_url)

        self.assertEqual(result, test_payload)


class TestClass:
    """class testclass"""
    def a_method(self):
        """method named a_method"""
        return 42

    @memoize
    def a_property(self):
        """method named a_property"""
        return self.a_method()


class TestMemoize(unittest.TestCase):
    """class to test using Memoization"""

    @patch.object(TestClass, 'a_method')
    def test_memoize(self, mock_a_method):
        """method to test method named memoize"""
        mock_a_method.return_value = 42

        test_instance = TestClass()

        result1 = test_instance.a_property
        result2 = test_instance.a_property

        mock_a_method.assert_called_once()

        self.assertEqual(result1, 42)
        self.assertEqual(result2, 42)

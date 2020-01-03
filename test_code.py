#!/usr/bin/env python

import unittest
import code


class TestSecrets(unittest.TestCase):
    def test_get_secrets_for_secret1_is_monkeys(self):
        result = code.get_secrets(["secret1"])
        expected = {"secret1": "monkeys"}
        self.assertEqual(expected, result)

    def test_get_secrets_for_secret2_is_dogs(self):
        result = code.get_secrets(["secret2"])
        expected = {"secret2": "dogs"}
        self.assertEqual(expected, result)

    def test_get_secrets_for_secret99_is_None(self):
        result = code.get_secrets(["secret99"])
        expected = {"secret99": None}
        self.assertEqual(expected, result)

    def test_get_secrets_for_secret1_and_secret99(self):
        result = code.get_secrets(["secret1", "secret99"])
        expected = {"secret1": "monkeys", "secret99": None}
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()

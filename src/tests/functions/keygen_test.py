import unittest

from functions.keygen import KeyGenerator


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self._key_generator = KeyGenerator()
        self._keys = self._key_generator.generate_keys()

    def test_key_generator_returns_a_dictionary(self):
        type_of_keys = type(self._keys)
        self.assertEqual(type_of_keys, dict)

    def test_key_dictionary_contains_three_items(self):
        items_in_keys = len(self._keys)
        self.assertEqual(items_in_keys, 3)

    def test_key_dictionary_contains_correct_items(self):
        n = self._keys["n"]
        type_of_n = type(n)
        self.assertEqual(type_of_n, int)

        e = self._keys["e"]
        type_of_e = type(e)
        self.assertEqual(type_of_e, int)

        d = self._keys["d"]
        type_of_d = type(d)
        self.assertEqual(type_of_d, int)

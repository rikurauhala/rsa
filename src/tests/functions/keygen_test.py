import sympy

import unittest

from functions.keygen import KeyGenerator


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self._key_generator = KeyGenerator()
        self._keys = self._key_generator.generate_keys()
        self._n = self._keys["n"]
        self._e = self._keys["e"]
        self._d = self._keys["d"]

    def test_key_generator_returns_a_dictionary(self):
        type_of_keys = type(self._keys)
        self.assertEqual(type_of_keys, dict)

    def test_key_dictionary_contains_three_items(self):
        items_in_keys = len(self._keys)
        self.assertEqual(items_in_keys, 3)

    def test_key_dictionary_contains_correct_items(self):
        type_of_n = type(self._n)
        self.assertEqual(type_of_n, int)

        type_of_e = type(self._e)
        self.assertEqual(type_of_e, int)

        type_of_d = type(self._d)
        self.assertEqual(type_of_d, int)

    def test_key_length_is_correct(self):
        actual_length = self._n.bit_length()
        expected_length = 1024
        self.assertEqual(actual_length, expected_length)

    def test_miller_rabin_returns_prime_numbers(self):
        bits = 1024
        probable_prime = self._key_generator._get_random_prime(bits)
        is_prime = sympy.isprime(probable_prime)
        self.assertTrue(is_prime)

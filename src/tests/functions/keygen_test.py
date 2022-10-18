import math
import random
import sympy
import unittest

from functions.keygen import KeyGenerator


class TestKeyGenerator(unittest.TestCase):
    def setUp(self):
        self._key_generator = KeyGenerator()
        self._key_length = 1024
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

    def test_n_has_expected_properties(self):
        for _ in range(10):
            p = self._key_generator._get_random_prime(self._key_length//2)
            q = self._key_generator._get_random_prime(self._key_length//2)
            n = self._key_generator._calculate_n(p, q)
            self.assertEqual(p.bit_length(), self._key_length//2)
            self.assertEqual(q.bit_length(), self._key_length//2)
            self.assertEqual(n.bit_length(), self._key_length)

    def test_phi_has_expected_properties(self):
        p = self._key_generator._get_random_prime(self._key_length//2)
        q = self._key_generator._get_random_prime(self._key_length//2)
        phi = self._key_generator._calculate_phi(p, q)
        self.assertEqual(phi, (p-1)*(q-1))
        self.assertEqual(math.gcd(self._e, phi), 1)

    def test_key_length_is_correct(self):
        actual_length = self._n.bit_length()
        self.assertEqual(actual_length, self._key_length)

    def test_miller_rabin_returns_prime_numbers(self):
        for _ in range(10):
            probable_prime = self._key_generator._get_random_prime(self._key_length)
            is_prime = sympy.isprime(probable_prime)
            self.assertTrue(is_prime)

    def test_divide_returns_quotient_and_remainder(self):
        quotient, remainder = self._key_generator._divide(3, 10)
        self.assertEqual(quotient, 3)
        self.assertEqual(remainder, 1)
        a = random.randint(0, 100000)
        b = random.randint(0, 100000)
        quotient, remainder = self._key_generator._divide(a, b)
        self.assertEqual(quotient, b // a)
        self.assertEqual(remainder, b % a)

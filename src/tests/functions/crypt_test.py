import unittest

from functions.crypt import Crypt
from functions.keygen import KeyGenerator

from utils.characters import CHARACTERS


class TestCrypt(unittest.TestCase):
    def setUp(self):
        self._characters = CHARACTERS
        self._crypt = Crypt()
        self._key_generator = KeyGenerator()
        self._keys = self._key_generator.generate_keys()
        self._message_m = "Hello, world!"
        self._message_c = self._crypt.encrypt(self._message_m, self._keys["e"], self._keys["n"])
        self._message_p = self._crypt.decrypt(self._message_c, self._keys["d"], self._keys["n"])

    def test_encryption_returns_integer(self):
        type_of_message_c = type(self._message_c)
        self.assertEqual(type_of_message_c, int)

    def test_decryption_returns_string(self):
        type_of_message = type(self._message_p)
        self.assertEqual(type_of_message, str)

    def test_decryption_succeeds(self):
        self.assertEqual(self._message_p, self._message_m)

    def test_supported_characters_can_be_used(self):
        message_m = ""
        for character in self._characters.values():
            message_m += character
        message_c = self._crypt.encrypt(message_m, self._keys["e"], self._keys["n"])
        message_p = self._crypt.decrypt(message_c, self._keys["d"], self._keys["n"])
        self.assertEqual(message_p, message_m)

    def test_unsupported_characters_cannot_be_used(self):
        message_m = "$"
        with self.assertRaises(KeyError, msg=f"Character {message_m} is not supported"):
            self._crypt.encrypt(message_m, self._keys["e"], self._keys["n"])

    def test_message_cannot_be_empty(self):
        message_m = ""
        with self.assertRaises(ValueError, msg="Message cannot be empty!"):
            self._crypt.encrypt(message_m, self._keys["e"], self._keys["n"])

    def test_convert_to_int(self):
        string = "abc"
        integer_actual = self._crypt._convert_to_int(string)
        integer_expected = 101112
        self.assertEqual(integer_actual, integer_expected)

    def test_convert_to_string(self):
        integer = 101112
        string_actual = self._crypt._convert_to_string(integer)
        string_expected = "abc"
        self.assertEqual(string_actual, string_expected)

    def test_message_maximum_length(self):
        message = ""
        for _ in range(154):
            message += "a"
            message_c = self._crypt.encrypt(message, self._keys["e"], self._keys["n"])
            message_p = self._crypt.decrypt(message_c, self._keys["d"], self._keys["n"])
            self.assertEqual(message_p, message)
        with self.assertRaises(ValueError, msg="Message is too long!"):
            message += "a"
            message_c = self._crypt.encrypt(message, self._keys["e"], self._keys["n"])
            message_p = self._crypt.decrypt(message_c, self._keys["d"], self._keys["n"])

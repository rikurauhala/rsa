import unittest

from functions.crypt import Crypt
from functions.keygen import KeyGenerator


class TestCrypt(unittest.TestCase):
    def setUp(self):
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

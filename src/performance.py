import rsa

from functions.crypt import Crypt
from functions.keygen import KeyGenerator


crypt = Crypt()
key_generator = KeyGenerator()
message = "Hello, world!"
key_length = 1024

def test_own_key_generation(benchmark):
    benchmark(key_generator.generate_keys)

def test_rsa_key_generation(benchmark):
    benchmark(rsa.newkeys, key_length)

def test_own_encryption(benchmark):
    keys = key_generator.generate_keys()
    benchmark(crypt.encrypt, message, keys["e"], keys["n"])

def test_rsa_encryption(benchmark):
    (public_key, private_key) = rsa.newkeys(key_length)
    message_encoded = message.encode('utf8')
    benchmark(rsa.encrypt, message_encoded, public_key)

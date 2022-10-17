import pytest
import rsa

from functions.crypt import Crypt
from functions.keygen import KeyGenerator


crypt = Crypt()
key_generator = KeyGenerator()
message = "Hello, world!"
key_length = 1024
rounds = 100

@pytest.mark.benchmark(min_rounds=rounds)
def test_key_generation_own(benchmark):
    benchmark(key_generator.generate_keys)

@pytest.mark.benchmark(min_rounds=rounds)
def test_key_generation_rsa(benchmark):
    benchmark(rsa.newkeys, key_length)

def test_encryption_own(benchmark):
    keys = key_generator.generate_keys()
    benchmark(crypt.encrypt, message, keys["e"], keys["n"])

def test_encryption_rsa(benchmark):
    (public_key, private_key) = rsa.newkeys(key_length)
    message_encoded = message.encode('utf8')
    benchmark(rsa.encrypt, message_encoded, public_key)

def test_decryption_own(benchmark):
    keys = key_generator.generate_keys()
    ciphertext = crypt.encrypt(message, keys["e"], keys["n"])
    benchmark(crypt.decrypt, ciphertext, keys["d"], keys["n"])

def test_decryption_rsa(benchmark):
    (public_key, private_key) = rsa.newkeys(key_length)
    message_encoded = message.encode('utf8')
    ciphertext = rsa.encrypt(message_encoded, public_key)
    benchmark(rsa.decrypt, ciphertext, private_key)

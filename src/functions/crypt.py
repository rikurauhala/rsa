class Crypt:
    """Used to encrypt and decrypt messages."""

    def __init__(self):
        """Initializes a new Crypt object."""

    def encrypt(self, m, e, n):
        """Encrypts a message.

        Args:
            m (int): Plaintext message to be encrypted.
            e (int): Public key encryption exponent.
            n (int): Public key modulus.

        Returns:
            c (int): Ciphertext message i.e. the encrypted message.
        """

        c = pow(m, e, n)
        return c

    def decrypt(self, c, d, n):
        """Decrypts a message.

        Args:
            c (int): Ciphertext message to be decrypted.
            d (int): Private key decryption exponent.
            n (int): Private key modulus.

        Returns:
            m (int): Plaintext message, i.e. the decrypted original message.
        """

        m = pow(c, d, n)
        return m

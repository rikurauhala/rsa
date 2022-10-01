class Crypt:
    """Used to encrypt and decrypt messages."""

    def __init__(self):
        """Initializes a new Crypt object."""

    def encrypt(self, m, e, n):
        """Encrypts a message.

        Args:
            m (integer): Plaintext message to be encrypted.
            e (integer): Public key encryption exponent.
            n (integer): Public key modulus.

        Returns:
            c (integer): Ciphertext message i.e. the encrypted message.
        """

        m = self._convert_to_int(m)
        c = pow(m, e, n)
        return c

    def decrypt(self, c, d, n):
        """Decrypts a message.

        Args:
            c (integer): Ciphertext message to be decrypted.
            d (integer): Private key decryption exponent.
            n (integer): Private key modulus.

        Returns:
            m (integer): Plaintext message, i.e. the decrypted original message.
        """

        m = pow(c, d, n)
        m = self._convert_to_string(m)
        return m

    def _convert_to_int(self, message):
        """Converts a string into a integer.

        Args:
            message (string): Message to be converted.

        Returns:
            m (integer): Encrypted message as an integer.
        """

        m = ""
        for char in message:
            m += str(ord(char)+100)
        return int(m)

    def _convert_to_string(self, message):
        """Converts an integer into a string.

        Args:
            message (string): Integer to be converted.

        Returns:
            message_str (string): Decrypted message as a string.
        """

        message_int = str(message)

        message_str = ""
        start, end = 0, 3

        while end <= len(message_int)+1:
            ascii_decimal = int(message_int[start:end])-100
            ascii_symbol = chr(ascii_decimal)
            message_str += ascii_symbol
            start += 3
            end += 3

        return message_str

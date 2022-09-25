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
            numbers = len(str(ord(char)))
            if numbers == 1:
                m += "00"
            elif numbers == 2:
                m += "0"
            m += str(ord(char))
        return int(m)

    def _convert_to_string(self, message):
        """Converts an integer into a string.

        Args:
            message (string): Integer to be converted.

        Returns:
            message_str (string): Decrypted message as a string.
        """

        message_int = str(message)
        message_length = len(message_int)

        if message_length % 3 != 0:
            if message_length % 2 == 0:
                message_int = "0" + message_int
            else:
                message_int = "00" + message_int

        message_str = ""
        start, end = 0, 3

        while end <= len(message_int)+1:
            ascii_decimal = message_int[start:end]
            if ascii_decimal[0] == 0:
                ascii_decimal = ascii_decimal[-2:]
            elif ascii_decimal[0] == 0 and ascii_decimal[1] == 0:
                ascii_decimal = ascii_decimal[-1]
            ascii_decimal = int(ascii_decimal)
            ascii_symbol = chr(ascii_decimal)
            message_str += ascii_symbol
            start += 3
            end += 3

        return message_str

class Crypt:
    """Used to encrypt and decrypt messages."""

    def __init__(self):
        pass

    def encrypt(self, m, n, e):
        c = (m**e) % n
        print(c)

    def decrypt(self, c, n, d):
        m = (c**d) % n
        print(m)

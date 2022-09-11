class KeyGenerator:
    """Used to generate public and private keys."""

    def __init__(self):
        pass

    def generate_keys(self):
        """Generates keys."""
        self._generate_public_key()
        self._generate_private_key()

    def _generate_public_key(self):
        """Generates a public key."""
        print("Generating public key")

    def _generate_private_key(self):
        """Generates a private key."""
        print("Generating private key")

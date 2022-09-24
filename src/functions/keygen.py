import random


class KeyGenerator:
    """Used to generate public and private keys."""

    def __init__(self):
        """Initializes a new KeyGenerator object."""

    def generate_keys(self):
        """Generates keys."""

        bit_length = 512

        p = self._get_random_prime(bit_length//2)
        q = self._get_random_prime(bit_length//2)

        n = p*q

        phi_n = (p-1)*(q-1)

        e = 65537
        d = self._modinv(e, phi_n)

        keys = {
            "n": n,
            "e": e,
            "d": d
        }

        print(f"Public key:  [ n: {n}, e: {e} ]")
        print(f"Private key: [ n: {n}, d: {d} ]")

        return keys

    def _get_random_prime(self, bits):
        """Generates a random probable prime number with desired bit length.

        Args:
            bits (int): Bit length of the prime, should be a power of two.

        Returns:
            n (int): A probable prime number.
        """

        while True:
            n = random.getrandbits(bits)
            if n % 2 == 0:
                n += 1
            n_is_prime = self._miller_rabin(n, 10)
            if n_is_prime:
                return n

    def _miller_rabin(self, n, k):
        """Tests the given number n for primality using the Miller-Rabin algorithm.

        Args:
            n (int): The number to be tested.
            k (int): The number of test rounds.

        Returns:
            boolean: Whether n is a probable prime or not.
        """

        d = n-1
        s = 0

        while d % 2 == 0:
            d >>= 1
            s += 1

        for _ in range(k):
            a = random.randrange(2, n-2)
            x = pow(a, d, n)
            if x in (1, n-1):
                continue
            for _ in range(s-1):
                x = pow(a, 2, n)
                if x == n-1:
                    continue
            return False

        return True

    def _modinv(self, a, b):
        _, x, _ = self._egcd(a, b)
        return x % b

    def _egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)

        q = b // a
        r = b % a
        g, x, y = self._egcd(r, a)
        return (g, y-q*x, x)

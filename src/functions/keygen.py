import math
import random
import secrets


class KeyGenerator:
    """Used to generate public and private keys."""

    def __init__(self):
        """Initializes a new KeyGenerator object."""

    def generate_keys(self):
        """Generates keys.

        Returns:
            keys (dictionary): {Key: string, value: integer} | Values of n, e and d
        """
        bit_length = 1024

        p = self._get_random_prime(bit_length//2)
        q = self._get_random_prime(bit_length//2)

        n = self._calculate_n(p, q)
        phi = self._calculate_phi(p, q)

        e = 65537
        d = self._modinv(e, phi)

        keys = {
            "n": n,
            "e": e,
            "d": d
        }

        return keys

    def _calculate_n(self, p, q):
        """Calculates the modulus part of the keys.

        Args:
            p (integer): A prime number.
            q (integer): A prime number.

        Returns:
            n (integer): The modulus.
        """
        n = p*q
        return n

    def _calculate_phi(self, p, q):
        """Calculates the totient.

        Euler totient function phi(n) = (p-1)(q-1).

        Args:
            p (integer): A prime number.
            q (integer): A prime number.

        Returns:
            phi (integer): The totient.
        """
        phi = (p-1)*(q-1)
        return phi

    def _get_random_integer(self, bits):
        """Generates a random integer with desired bit length.

        A secure random number generator is used by utilizing the secrets module.
        A random integer is generated from a range of 1.5 * 2^(bits-1) to 2^bits.
        For example if the desired bit length is 1024, the range would go from
        1.5 * 2^1023 to 2^1024. This way the generated integer will (almost) always
        have the desired bit length.

        Args:
            bits (integer): Bit length of the number, should be a power of two.

        Returns:
            random_integer (integer): A random integer.
        """
        secure_rng = secrets.SystemRandom()
        start = math.floor(1.5*2**(bits-1))
        stop = 2**bits
        random_integer = secure_rng.randrange(start, stop)
        return random_integer

    def _get_random_prime(self, bits):
        """Generates a random probable prime number with desired bit length.

        Note that the algorithm is probabilistic in nature and the number
        returned is only a (highly) probable prime.

        Args:
            bits (integer): Bit length of the prime, should be a power of two.

        Returns:
            n (integer): A probable prime number.
        """
        while True:
            n = self._get_random_integer(bits)
            if n % 2 == 0:
                n += 1
            n_is_prime = self._miller_rabin(n, 64)
            if n_is_prime:
                return n

    def _miller_rabin(self, n, k):
        """Tests the given number n for primality using the Miller-Rabin algorithm.

        Args:
            n (integer): The number to be tested.
            k (integer): The number of test rounds.

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
        """Calculates the modular inverse.

        Args:
            a (integer)
            b (integer)

        Returns:
            integer
        """
        s = self._egcd(a, b)
        return s % b

    def _divide(self, a, b):
        """Divides two integers, returns the quotient and the remainder.

        Performs Euclidean division.

        Args:
            a (integer): Divident.
            b (integer): Divisor.

        Returns:
            quotient, remainder (tuple)
        """
        quotient = b // a
        remainder = b % a
        return (quotient, remainder)

    def _egcd(self, a, b):
        """Implements the extended Euclidean algorithm.

        Only the value s is returned as only that value is needed by the program.

        Args:
            a (integer)
            b (integer)

        Returns:
            s (integer)
        """
        s, old_s = 0, 1
        t, old_t = 1, 0
        while a != 0:
            quotient, remainder = self._divide(a, b)
            m = s - t * quotient
            n = old_s - old_t * quotient
            b, a = a, remainder
            s, old_s = t, old_t
            t, old_t = m, n
        return s

import random


class KeyGenerator:
    """Used to generate public and private keys."""

    def __init__(self):
        pass

    def generate_keys(self):
        """Generates keys."""

        bit_length = 1024

        p = self._get_random_prime(bit_length//2)
        q = self._get_random_prime(bit_length//2)

        n = p*q
        
        lambda_n = self._lcm(p-1, q-1)
        phi_n = (p-1) * (q-1)

        # e is usually 65537
        e = 3

        # d should be calculated
        d = 7

        keys = {
            "n": n,
            "e": e,
            "d": d
        }

        print(f"p: {p}")
        print(f"q: {q}")
        #print(f"Public key:  [ n: {n}, e: {e} ]")
        #print(f"Private key: [ n: {n}, d: {d} ]")

        return keys

    def _get_random_prime(self, bits):
        while True:
            n = random.getrandbits(bits)
            if n % 2 == 0:
                n += 1
            n_is_prime = self._miller_rabin(n, 10)
            if n_is_prime:
                return n


    def _miller_rabin(self, n, k):
        d = n-1
        s = 0

        while d % 2 == 0:
            d >>= 1
            s += 1

        for _ in range(k):
            a = random.randrange(2, n-2)
            x = pow(a, d, n)
            if x == 1 or x == n-1:
                continue
            for _ in range(s-1):
                x = pow(a, 2, n)
                if x == n-1:
                    continue
            return False

        return True


    def _lcm(self, a, b):
        return ( len(str(a)) * len(str(b)) ) / self._gcd(a, b)

    def _gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self._gcd(b, a % b)

class KeyGenerator:
    """Used to generate public and private keys."""

    def __init__(self):
        pass

    def generate_keys(self):
        """Generates keys."""

        # Large prime numbers should be used for p and q
        p = 11
        q = 3

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

        print(f"Public key:  [ n: {n}, e: {e} ]")
        print(f"Private key: [ n: {n}, d: {d} ]")

        return keys

    def _lcm(self, a, b):
        return ( len(str(a)) * len(str(b)) ) / self._gcd(a, b)

    def _gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self._gcd(b, a % b)

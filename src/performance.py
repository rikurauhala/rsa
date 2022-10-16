import rsa
import time

from functions.keygen import KeyGenerator


class PerformanceTest:
    """Used to test the performance of the application and its algorithms.
    
    Performance is measured against the Python rsa module with the same parameters.
    Can be run with "poetry run invoke performance-test" from the console.
    """

    def __init__(self):
        """Initializes a new Performance test."""
        self._key_length = 1024
        self._rounds = 100
        self._key_generator = KeyGenerator()

    def run(self):
        """Runs the performance test.
        
        Mode 1: This application.
        Mode 2: The rsa module.
        """
        print("Running the performance test.")
        self._test_key_generation(1)
        self._test_key_generation(2)

    def _test_key_generation(self, mode):
        """Tests the performance of key generation.

        Args:
            mode (integer)
        """
        print(f"Testing key generation, mode {mode}.")
        values = []
        for round in range(self._rounds):
            if round % 10 == 0:
                print(f"Round {round} / {self._rounds}")
            start = time.time()
            if mode == 1:
                self._key_generator.generate_keys()
            if mode == 2:
                rsa.newkeys(1024)
            end = time.time()
            time_ms = (end-start) * 10**3
            values.append(time_ms)
        average = sum(values) / len(values)
        print(f"The average execution time was {average} ms based on {self._rounds} rounds.")

if __name__ == "__main__":
    performance_test = PerformanceTest()
    performance_test.run()

import rsa
import time


class PerformanceTest:
    """Used to test the performance of the application and its algorithms.
    
    Performance is measured against the Python rsa module with the same parameters.
    Can be run with "poetry run invoke performance-test" from the console.
    """

    def __init__(self):
        """Initializes a new Performance test."""
        self._key_length = 1024
        self._rounds = 100

    def run(self):
        """Runs the performance test."""
        print("Running the performance test.")
        self._test_key_generation()

    def _test_key_generation(self):
        values = []
        for _ in range(self._rounds):
            start = time.time()
            rsa.newkeys(1024)
            end = time.time()
            time_ms = (end-start) * 10**3
            values.append(time_ms)
        average = sum(values) / len(values)
        print(f"The average execution time was {average} ms based on {self._rounds} rounds.")


if __name__ == "__main__":
    performance_test = PerformanceTest()
    performance_test.run()

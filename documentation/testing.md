# Testing

## Overview

Automated tests has been written using [pytest](https://docs.pytest.org/en/7.1.x). A test coverage report can be generated with [coverage](https://coverage.readthedocs.io/en/6.5.0/).

## Unit testing

### Running unit tests

```bash
# Tests can be run with the command
$ poetry run invoke test
```

### Test coverage

```bash
# Test coverage can be checked with the command
$ poetry run invoke coverage

# A test coverage report can be generated with the command
$ poetry run invoke coverage-report

# The coverage report can be viewed by opening it
# with a web browser, for example Mozilla Firefox
$ firefox htmlcov/index.html
```

#### Coverage report

Coverage report: 97%
*coverage.py v6.4.4, created at 2022-10-11 20:00 +0300*

| Module 	                 | statements |	missing | excluded | branches | partial | coverage |
| :------------------------- | ---------: | ------: | -------: | -------: | ------: | -------: |
| src/functions/crypt.py 	 |         30 |       0 |        0 |        8 |       0 |     100% |
| src/functions/keygen.py 	 |         64 |       1 |        0 |       18 |       1 |      98% |
| src/utils/character_map.py | 	       17 |       1 |        0 |       10 |       1 |      93% |
| src/utils/dictionary.py    |          1 |       0 |        0 |        0 |       0 |     100% |
| **Total**                  |    **112** |   **2** |    **0** |   **36** |   **2** |  **97%** |

## Performance testing

Performance tests have been implemented in a separate module and they can be found in the file `src/performance.py`. The performance of the application is tested by comparing it to [another implementation](https://github.com/sybrenstuvel/python-rsa) with the same input parameters. The add-on [pytest-benchmark](https://pytest-benchmark.readthedocs.io/en/stable/index.html) is used for benchmarking.

### Running the performance test

```bash
# The performance test can be run with the following command
# Please be patient as it may take some time to finish
$ poetry run invoke performance-test
```

### Results

| Name (time in ms)       |                  Min |                  Max |               Mean |             StdDev |             Median |                IQR | Outliers |                OPS |    Rounds |
| :---------------------- | -------------------: | -------------------: | -----------------: | -----------------: | -----------------: | -----------------: | -------: | -----------------: | --------: |
| test_decryption_own     |     3.4786 (95.54)   |     5.7416 (52.53)   |   3.9351 (104.80)  |   0.7447 (165.39)  |   3.5542 (96.86)   |   0.1720 (>1000.0) |    61;61 |    254.1257 (0.01) |       283 |
| test_decryption_rsa     |     1.2088 (33.20)   |     1.5862 (14.51)   |   1.2372 (32.95)   |   0.0390 (8.66)    |   1.2210 (33.27)   |   0.0360 (262.42)  |    52;24 |    808.2678 (0.03) |       597 |
| test_encryption_own     |     0.0364 (1.0)     |     0.1093 (1.0)     |   0.0375 (1.0)     |   0.0045 (1.0)     |   0.0367 (1.0)     |   0.0001 (1.0)     | 692;2121 | 26,632.2482 (1.00) |     19494 |
| test_encryption_rsa     |     0.0475 (1.30)    |     0.1233 (1.13)    |   0.0496 (1.32)    |   0.0059 (1.31)    |   0.0484 (1.32)    |   0.0004 (2.71)    | 649;1052 | 20,151.8147 (0.76) |     14928 |
| test_key_generation_own |   111.9827 (>1000.0) | 1,856.7336 (>1000.0) | 522.0810 (>1000.0) | 319.4778 (>1000.0) | 461.7929 (>1000.0) | 367.8679 (>1000.0) |     22;4 |      1.9154 (0.00) |       100 |
| test_key_generation_rsa |    35.7842 (982.81)  | 1,339.8350 (>1000.0) | 295.5723 (>1000.0) | 250.4264 (>1000.0) | 239.3908 (>1000.0) | 264.4683 (>1000.0) |     16;5 |      3.3833 (0.00) |       100 |

Legend:
- Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
- OPS: Operations Per Second, computed as 1 / Mean

## Known issues

See [Issues](https://github.com/rikurauhala/rsa/issues) for an up-to-date list.

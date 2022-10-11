# Testing

## Overview

Automated tests has been written using [pytest](https://docs.pytest.org/en/7.1.x). A test coverage report can be generated with [coverage](https://coverage.readthedocs.io/en/6.5.0/).

## Running tests

```bash
# Tests can be run with the command
$ poetry run invoke test
```

## Test coverage

```bash
# Test coverage can be checked with the command
$ poetry run invoke coverage

# A test coverage report can be generated with the command
$ poetry run invoke coverage-report

# The coverage report can be viewed by opening it
# with a web browser, for example Mozilla Firefox
$ firefox htmlcov/index.html
```

### Coverage report

Coverage report: 97%
*coverage.py v6.4.4, created at 2022-10-11 20:00 +0300*

| Module 	                 | statements |	missing | excluded | branches | partial | coverage |
| :------------------------- | ---------: | ------: | -------: | -------: | ------: | -------: |
| src/functions/crypt.py 	 |         30 |       0 |        0 |        8 |       0 |     100% |
| src/functions/keygen.py 	 |         64 |       1 |        0 |       18 |       1 |      98% |
| src/utils/character_map.py | 	       17 |       1 |        0 |       10 |       1 |      93% |
| src/utils/dictionary.py    |          1 |       0 |        0 |        0 |       0 |     100% |
| **Total**                  |    **112** |   **2** |    **0** |   **36** |   **2** |  **97%** |

## Known issues

See [Issues](https://github.com/rikurauhala/rsa/issues) for an up-to-date list.

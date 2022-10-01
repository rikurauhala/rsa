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

![Coverage report](/documentation/images/coverage-report.png)

## Known issues

- Strong messages aren't supported yet

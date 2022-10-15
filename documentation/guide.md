# User guide

## Installing

Start by getting the source code and installing dependencies. [Poetry](https://python-poetry.org/) should be installed on your machine. More information about Poetry and dependencies can be found [here](https://ohjelmistotekniikka-hy.github.io/python/viikko2#poetry-ja-riippuvuuksien-hallinta) (in Finnish).

Please note that Python **version 3.8** or later should be used. You may want to look into [pyenv](https://github.com/pyenv/pyenv) to switch to the correct version.

```bash
# Get the source code
$ git clone git@github.com:rikurauhala/rsa.git

# Change directory
$ cd rsa

# Install dependencies
$ poetry install
```

## Running

The application can be started by running the start command. The application has a straightforward commandline interface. The command list will be printed after starting the application or by typing `h`. 

```bash
# Run the application
$ poetry run invoke start
```

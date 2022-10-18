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

The application can be started by running the start command. The application has a straightforward commandline interface. 

```bash
# Run the application
$ poetry run invoke start
```

## Commands

The application has the following commands. Commands can be given by running the application and typing them in the command-line interface after the green `>` symbol. The list of commands can be found here or by typing the command `h` (short for *help*).

```
Commands:
[ q ] quit
[ h ] print the command list
[ 1 ] generate keys
[ 2 ] encrypt message
[ 3 ] decrypt message
[ 4 ] show public key
[ 5 ] show private key
```

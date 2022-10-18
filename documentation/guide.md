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

The application has the following commands. Commands can be given by running the application and typing them in the command-line interface after the green `>` symbol. The list of commands can be found here or by typing the command `h` (short for *help*). The command list below is also printed after running the application.

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

## Functionality

This section contains instructions on how to use the application. For the technical details, see the [implementation](implementation.md) document. The application can be terminated with the command `q` (short for *quit*).

### Key generation

Keys can be generated with the command `1.` The application will indicate while keys are being generated and when it's done. This should not take too long, however. The keys are stored in the application memory and can be viewed with the commands `4` and `5`.

### Encrypting a message

A message can be encrypted by entering the command `2` and entering a plaintext message. For the list of supported characters, see [here](implementation.md#charactermap). If the message contains unsupported characters or is too long, an error message will be displayed.

### Decrypting a message

The encrypted message can be decrypted by typing the command `3`. The message is stored in the memory, so there is no need to copy and paste the encrypted ciphetext here.

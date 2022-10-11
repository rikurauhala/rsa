# Implementation

## Overview

The program implements a simple version of the [RSA cryptosystem](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) in Python. The application has a command-line interface. It offers functionality for generating (both public and private) keys and using them to encrypt and decrypt messages.

[Poetry](https://python-poetry.org/) is used for managing dependencies and the commands for various *tasks* are handled by [Invoke](https://www.pyinvoke.org/).

## Data structures and algorithms

Multiple different algorithms are implemented. Together they form a working program.

### Key generation

The following algorithm is used to generate the public and the private key. All functionality is implemented in the file `src/functions/keygen.py`.

1. Choose a desired *key length*.
    - Should be a power of two, usually $2^{10} = 1024$, $2^{11} = 2048$ or $2^{12} = 4096$.
    - Greater key length permits longer messages and offers stronger encryption but key generation will take longer.
2. Choose two *distinct* prime numbers, $p$ and $q$.
    - These values are to be kept secret and disposed of after key generation.
    - The *bit length* of each should be half the key length chosen in step 1.
    - Large prime numbers can be found efficiently using the *Miller-Rabin* test.
3. Calculate $n = pq$.
    - $n$ is the *modulus*, used for both keys. It will be made public.
    - The bit length of $n$ should match the key length chosen in step 1.
4. Calculate $\phi(n) = (p-1)(q-1)$.
    - The value will be kept secret and forgotten after key generation.
5. Choose an integer $e$, so that $e$ and $\phi$ are *coprime* and $1 < e < \phi$.
    - Usually $2^{16} = 65537$ is a good choice and my implementation also uses this value.
6. Calculate $d$.
    - $d$ can be calculated using the *extended Euclidean algorithm*.
    - $d$ is the exponent part of the *private key* and should **not** be published anywhere.

To summarize:
- The public key is made of the modulus $n$ and the *encryption exponent* $e$.
- The private key consists of $n$ and the *decryption exponent* $d$.

#### Primality test

To be written.

### Encryption and decryption

All functionality is implemented in the file `src/functions/crypt.py`.

#### Encrypting a message

A message can be encrypted with the following procedure.

1. Enter a plaintext message.
2. Convert the message into an integer.
    - Conversion is done using the custom CharacterMap object, see below.
3. Encrypt the message.
    - The message can be encrypted by calculating  $c \equiv m^{e}$ (mod $n$), where
        - $c$ is the encrypted ciphertext
        - $m$ is the plaintext to be encrypted
        - $e$ is the public encryption exponent
        - $n$ is the modulus

#### Decrypting a message

A message can be decrypted with the following procedure.

1. Enter the decrypted message.
    - In the context of this program, the message is stored in memory.
2. Decrypt the message.
    - The message can be decrypted by calculating, $c^{d} \equiv (m^{e})^{d} \equiv m$ (mod $n$) where
        - $c$ is the encrypted ciphertext
        - $m$ is the original plaintext
        - $e$ is the public encryption exponent
        - $d$ is the private decryption exponent
        - $n$ is the modulus
3. Convert the decrypted message into a string.
    - Conversion is done using the custom CharacterMap object, see below.

#### CharacterMap

CharacterMap is a custom data structure that is used to map characters into corresponding order numbers and vice versa. It works in a similar way to Python's built-in `ord()` and `str()` functions. It is needed to convert string to integers for encryption and decryption. CharacterMap offers only a limited set of characters, but it permits longer messages to be encrypted. The implementation can be found in the file `src/utils/character_map.py`.

The *integer-character* value pairs are stored in a dictionary in the file `src/utils/dictionary.py`. It has the followings contents, meaning only these characters are supported by the application.
The character set is a subset of the ASCII encoding standard.

|  # | char |  # | char |  # | char |
| -: | :--: | -: | :--: | -: | :--: |
| 10 |    a | 40 |    A | 70 |    0 |
| 11 |    b | 41 |    B | 71 |    1 |
| 12 |    c | 42 |    C | 72 |    2 |
| 13 |    d | 43 |    D | 73 |    3 |
| 14 |    e | 44 |    E | 74 |    4 |
| 15 |    f | 45 |    F | 75 |    5 |
| 16 |    g | 46 |    G | 76 |    6 |
| 17 |    h | 47 |    H | 77 |    7 |
| 18 |    i | 48 |    I | 78 |    8 |
| 19 |    j | 49 |    J | 79 |    9 |
| 20 |    k | 50 |    K | 80 |    ! |
| 21 |    l | 51 |    L | 81 |    % |
| 22 |    m | 52 |    M | 82 |    & |
| 23 |    n | 53 |    N | 83 |    ( |
| 24 |    o | 54 |    O | 84 |    ) |
| 25 |    p | 55 |    P | 85 |    * |
| 26 |    q | 56 |    Q | 86 |    + |
| 27 |    r | 57 |    R | 87 |    , |
| 28 |    s | 58 |    S | 88 |    - |
| 29 |    t | 59 |    T | 89 |    . |
| 30 |    u | 60 |    U | 90 |    / |
| 31 |    v | 61 |    V | 91 |    : |
| 32 |    w | 62 |    W | 92 |    ; |
| 33 |    x | 63 |    X | 93 |    < |
| 34 |    y | 64 |    Y | 94 |    > |
| 35 |    z | 65 |    Z | 95 |    = |
| 36 |    å | 66 |    Å | 96 |    ? |
| 37 |    ä | 67 |    Ä | 97 |    @ |
| 38 |    ö | 68 |    Ö | 98 |    _ |
| 39 |      | 69 |    " | 99 |    € |

## Time and space complexities

To be written.

## Testing

See the [testing document](testing.md) for more details.

## Project structure

The project has the following file structure. All documentation can be found in the `documentation` directory. The contents of `htmlcov` are generated by the *coverage* command. The only relevant file there is *index.html* and it should be opened in a web browser to inspect the test coverage. The directory `src` contains the source code of the program, including automated tests. The file *index.py* is the entry point and the file *app.py* contains the main application loop logic and user interface code.

As the project is managed by Poetry, the directory contains the configuration files *poetry.lock* and *pyproject.toml*. They are needed to install dependencies. See the user manual for instructions. The file *tasks.py* is used by the dependency Invoke, which is used to define commands for Poetry. And as expected, *README.md* contains relevant information about the repository and is displayed on the project's GitHub page.

```
├── documentation
│   ├── images
│   │   └── coverage-report.png
│   ├── reports
│   │   ├── week1.md
│   │   ├── ...
│   │   └── week6.md
│   ├── guide.md
│   ├── implementation.md
│   ├── specification.md
│   └── testing.md
├── htmlcov
│   ├── ...
│   ├── index.html
│   └── ...
├── src
│   ├── functions
│   │   ├── __init__.py
│   │   ├── crypt.py
│   │   └── keygen.py
│   ├── tests
│   │   ├── functions
│   │   │   ├── __init__.py
│   │   │   ├── crypt_test.py
│   │   │   ├── keygen_test.py
│   │   └── __init__.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── character_map.py
│   │   └── dictionary.py
│   ├── app.py
│   ├── console_io.py
│   └── index.py
├── .coverage
├── .coveragerc
├── .gitignore
├── .pylintrc
├── .python-version
├── poetry.lock
├── pyproject.toml
├── README.md
└── tasks.py
```

## Sources

The following sources have been used in the development process.

- [ASCII Code](https://www.ascii-code.com/) (n.d.) | ascii-code.com
- [Coprime integers](https://en.wikipedia.org/wiki/Coprime_integers) (n.d.) | wikipedia.org
- [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) (n.d.) | wikipedia.org
- [Euclidean division](https://en.wikipedia.org/wiki/Euclidean_division) (n.d.) | wikipedia.org
- [Extended Euclidean algorithm](https://brilliant.org/wiki/extended-euclidean-algorithm/) (n.d.) | brilliant.org
- [Extended Euclidean algorithm](https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm) (n.d.) | wikipedia.org
- [Miller–Rabin primality test](https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test) (n.d.) | rosettacode.org
- [Miller-Rabin primality test](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test) (n.d.) | wikipedia.org
- [Public Key Cryptography: RSA Encryption Algorithm](https://www.youtube.com/watch?v=wXB-V_Keiu8) (2012) | Art of the Problem on youtube.com
- [RSA (cryptosystem)](https://en.wikipedia.org/wiki/RSA_(cryptosystem)) (n.d.) | wikipedia.org
- [RSA - bitlength of p and q](https://stackoverflow.com/questions/12192116/rsa-bitlength-of-p-and-q/12195783#12195783) (2012) | Mark Dickinson on stackoverflow.com
- [RSA Encryption](https://brilliant.org/wiki/rsa-encryption/) (n.d.) | brilliant.org

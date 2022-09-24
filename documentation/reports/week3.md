# Week 3

## Weekly report

This week I didn't have much time to work on the project but I managed to implement an initial  version of the core functionality. The Miller-Rabin primality test has been implemented based on [this pseudocode example](https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#Miller%E2%80%93Rabin_test). However, the Miller-Rabin test alone appears to be quite slow for generating primes with a bit length of 1024 or 2048. This step could probably be boosted by combining with sieving or other methods.

I had some problems with understanding the details but I also learned a lot. I need to look more into the extended Eucledian algorithm. There seems to be multiple ways of doing it and there could be ways to improve its implementation.

The plan for the next week is to improve the current state of the program and write unit tests.

## Work hours

|       date |  hours | description                                                          |
| ---------: | -----: | :------------------------------------------------------------------- |
| 2022-09-21 |      1 | researching, experimenting with code                                 |
| 2022-09-22 |      1 | researching, experimenting with code                                 |
| 2022-09-24 |      6 | implementing Miller-Rabin and extended Eucledian algorithm           |
|      total |      8 |                                                                      |

# Week 5

## Weekly report

This week's work was mostly based on the brilliant [peer review](https://github.com/rikurauhala/rsa/issues/3) written by fellow student [Vili Sinervä](https://github.com/ArcticCoder). He pointed out several flaws with the program and I was able to improve a lot based on the valuable feedback received.

I managed to solve several issues with the program. The bit length of the keys should now (most of the time anyway) remain constant and not vary too much based on the random component of the algorithm.

There is still work to be done. Using a 4096-bit key might be desirable but in the current state of the program, generating keys can take up to half a minute. The key generation process could be sped up. Documentation also still needs work and as the implementation is nearing completion, I should calculate the time and space complexities for different parts of the procedure. Also, the program needs more validation and testing, there are some cases where it straight up crashed and it is urgent to pay more attention to these issues towards the end of the course.

## Work hours

|       date |  hours | description                                                          |
| ---------: | -----: | :------------------------------------------------------------------- |
| 2022-10-02 |      1 | making minor improvements                                            |
| 2022-10-07 |      3 | improving the program based on the peer review                       |
| 2022-10-08 |      6 | improving the program, writing documentation                         |
|      total |     10 |                                                                      |

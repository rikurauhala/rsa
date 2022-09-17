# Week 2

## Weekly report

This week I did some research on how the RSA cryptosystem works and how it could be implemented in Python. I think at this point I have a decent understanding of how the system works as a whole, but the details still seem bit too complicated for me. The topic is quite heavy on maths and I would prefer to understand what I'm doing so the task requires a lot of thought. Different sources have conflicting information or don't provide clear enough instructions.

A basic commandline interface has been created. I also managed to implement a very basic version of the algorithm with some handpicked, simple values. No tests yet, as the program doesn't do much actual calculation just yet.

Next week I am going to work on improving the implementation. I wrote down a list of problems to solve:

- Generating large enough prime numbers for $p$ and $q$
  - Fermat test?
  - Miller-Rabin?
- Using $65537$ as $e$ would be good enough but the program should allow for other values to add complexity
- Using $\phi(n)$ or $\lambda(n)$?
  - The latter would add complexity but would probably not make the program any better
- Calculating $d$ properly
  - Another algorithm is needed for this part
- Converting messages to integers and from integers back to strings

## Work hours

|       date |  hours | description                                                          |
| ---------: | -----: | :------------------------------------------------------------------- |
| 2022-09-11 |      5 | creating a command-line interface, researching the topic             |
| 2022-09-15 |      1 | researching the topic, experimenting with code                       |
| 2022-09-16 |      2 | researching the topic, experimenting with code                       |
| 2022-09-17 |      3 | researching the topic, implementing a basic version                  |
|      total |     11 |                                                                      |

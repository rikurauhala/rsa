# Week 6

## Weekly report

This week I focused on the documentation and writing more unit tests. The program works as intended and I could call it ready, but as there is still time to work on it, I will try to make some improvements. I've found it hard to optimize the speed, but I will look more into it. Also, more testing is still required.

Writing the performance tests was started this week. The idea is to compare the performance to another RSA implementation in Python.

Python version was downgraded from 3.10.2 to 3.8 because of compatibility issues. I tried upgrading the key length to 2048 but it turned out to be harder than expected and started to cause some issues. So for now, the key length will stay at 1024 bits. This may still change if I can figure out how to solve the issues related to it.

## Work hours

|       date |  hours | description                                                          |
| ---------: | -----: | :------------------------------------------------------------------- |
| 2022-10-09 |      1 | making minor improvements, writing documentation                     |
| 2022-10-10 |      2 | writing documentation, working on a custom character map structure   |
| 2022-10-11 |      7 | writing documentation and tests, fixing issues                       |
| 2022-10-12 |      1 | writing tests, fixing issues                                         |
| 2022-10-15 |      3 | writing documentation and tests, fixing issues                       |
|      total |     14 |                                                                      |

#!/usr/bin/env python3
#
# Generate some prime numbers
#

import math

def primes(output, maxprime):
    count = 3

    while True:
        isprime = True

        for x in range(2, int(math.sqrt(count) + 1)):
            if count % x == 0:
                isprime = False
                break

        if isprime:
            print(count, file=output)

        count += 1

        if count > maxprime:
            return

f = open('output.txt', 'w')
primes(f, 100)

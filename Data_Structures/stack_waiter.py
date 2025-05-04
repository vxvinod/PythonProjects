#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#


def return_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def waiter(number, q):
    answers = []
    primes = []
    n = 2

    while len(primes) < q:
        if return_prime(n):
            primes.append(n)
        n += 1

    for i in range(q):
        prime = primes[i]
        a = []
        b = []

        for val in number[::-1]:
            if val % prime == 0:
                b.append(val)
            else:
                a.append(val)

        answers.extend(reversed(b))
        number = a

    answers.extend(reversed(number))
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = int(first_multiple_input[0])
    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))
    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

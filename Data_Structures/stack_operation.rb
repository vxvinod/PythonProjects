#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    # Write your code here
    arr = []
    result = []
    ret_arr = []
    for opn in operations:
        op = opn.split(" ")
        if op[0] == "1":
            val = int(op[1])
            arr.append(val)
            if not ret_arr or val >= ret_arr[-1]:
                ret_arr.append(val)
        elif op[0] == "2":
            popped = arr.pop()
            if popped == ret_arr[-1]:
                ret_arr.pop()
        elif op[0] == "3":
            result.append(ret_arr[-1])

    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

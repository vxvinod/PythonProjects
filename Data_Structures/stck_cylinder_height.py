#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce


#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Write your code here
    cylinder = {}
    cylinder["h1"] = reduce(lambda x, y: x + y, h1)
    cylinder["h2"] = reduce(lambda x, y: x + y, h2)
    cylinder["h3"] = reduce(lambda x, y: x + y, h3)
    print(cylinder)
    for i in range(1, 4, 1):
        # h1_min_val = min(cylinder["h1"].values())
        # h2_min_val = min(cylinder["h2"].values())
        # h3_min_val = min(cylinder["h3"].values())
        # min_val = min(h1_min_val, h2_min_val, h3_min_val)

        min_cyl = []
        while True:
            print("Cylindersss", cylinder)
            min_val = min(cylinder.values())
            print("min val", min_val)
            min_cyl = []
            for k, v in cylinder.items():
                if v == min_val:
                    min_cyl.append(k)
            print(min_cyl)

            for k, v in cylinder.items():
                if len(min_cyl) == 3:
                    return min_val
                if k not in min_cyl:
                    print("popping", k)
                    val = globals()[k].pop(0)
                    print("popped value", val)
                    cylinder[k] -= val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()

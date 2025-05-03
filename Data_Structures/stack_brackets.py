#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    b = {'}': '{', ']': '[', ')': '('}
    print(s)
    bracks = list(s)
    s_brack = []
    for brack in bracks:
        if brack in ['{', '[', '(']:
            s_brack.append(brack)
        elif not s_brack or b.get(brack) != s_brack[-1]:
            return 'NO'
        elif b.get(brack, None) == s_brack[-1]:
            s_brack.pop(-1)
        else:
            return 'NO'

    if len(s_brack) == 0:
        return 'YES'
    else:
        return 'NO'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()

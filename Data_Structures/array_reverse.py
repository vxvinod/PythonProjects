'''
HACKER RANK: DATA STRUCTURES
An array is a data structure that stores elements of the same type in a contiguous block of memory. In an array, , of size , each memory location has some unique index,  (where ), that can be referenced as  or .

Your task is to reverse an array of integers.

Note: If you've already solved our C++ domain's Arrays Introduction challenge, you may want to skip this.

Example

Return .

Function Description

Complete the function  with the following parameter(s):

: the array to reverse
Returns

: the reversed array
Input Format

The first line contains an integer, , the number of integers in .
The second line contains  space-separated integers that make up .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def reverseArray(a):
    # Write your code here
    a_reverse = []
    for i in range(len(a)-1, -1, -1):
        a_reverse.append(a[i])
    return a_reverse
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

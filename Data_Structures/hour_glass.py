#!/bin/python3
'''
Given a  2D array, , an hourglass is a subset of values with indices falling in the following pattern:

a b c
  d
e f g
There are  hourglasses in a  array. The  is the sum of the values in an hourglass. Calculate the hourglass sum for every hourglass in , then print the  hourglass sum.

Example


-9 -9 -9  1 1 1
 0 -9  0  4 3 2
-9 -9 -9  1 2 3
 0  0  8  6 6 0
 0  0  0 -2 0 0
 0  0  1  2 4 0
The  hourglass sums are:

-63, -34, -9, 12,
-10,   0, 28, 23,
-27, -11, -2, 10,
  9,  17, 25, 18
The highest hourglass sum is  from the hourglass beginning at row , column :

0 4 3
  1
8 6 6
Note: If you have already solved the Java domain's Java 2D Array challenge, you may wish to skip this challenge.

Function Description

Complete the function  with the following parameter(s):

: a 2-D array of integers
Returns

: the maximum hourglass sum
Input Format

Each of the  lines of inputs  contains  space-separated integers .
'''
import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    max_list = []
    arr_size = len(arr)
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if i+1 < arr_size and i+2 < arr_size and j+1 < arr_size and j+2 < arr_size:
                top = arr[i][j]+arr[i][j+1]+arr[i][j+2]
                middle = arr[i+1][j+1]
                bottom = arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
                max_list.append(top+middle+bottom)
    return max(max_list)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

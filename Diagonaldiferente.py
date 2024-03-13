import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    diagonal_primary = 0
    diagonal_secondary = 0
    for i in range(len(arr)):
        diagonal_primary += arr[i][i]
        diagonal_secondary += arr[i][len(arr) - i - 1]
    difference = abs(diagonal_primary - diagonal_secondary)
    
    return difference

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
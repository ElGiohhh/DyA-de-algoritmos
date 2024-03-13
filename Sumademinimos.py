import math
import os
import random
import re
import sys

def plusMinus(arr):
    positive_count = 0
    negative_count = 0
    zero_count = 0
    for num in arr:
        if num > 0:
            positive_count += 1
        elif num < 0:
            negative_count += 1
        else:
            zero_count += 1

    total_count = len(arr)
    positive_ratio = positive_count / total_count
    negative_ratio = negative_count / total_count
    zero_ratio = zero_count / total_count
    print("{:.6f}".format(positive_ratio))
    print("{:.6f}".format(negative_ratio))
    print("{:.6f}".format(zero_ratio))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
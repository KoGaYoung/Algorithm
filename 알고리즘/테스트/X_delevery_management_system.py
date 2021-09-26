#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'widestGap' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY start
#  3. INTEGER_ARRAY finish
#

def widestGap(n, start, finish):
    # Write your code here (solve 3/14)
    a = [0 for _ in range(n)]
    for idx, item in enumerate(start):
        for i in range(start[idx] - 1, finish[idx]):
            a[i] = 1

    # print(''.join([str(i) for i in a]).split('1'))

    s = ''.join([str(i) for i in a]).split('1')
    # s = list(filter(lambda x: x!='', s))
    len_s = [len(i) for i in s]
    print(max(len_s))

    # print(''.join(s))

if __name__ == '__main__':
    # widestGap(10, [1,2,5,8], [2,2,6,10])
    # widestGap(10, [3, 8], [4, 9])
    # widestGap(10, [1, 2, 6, 6], [4,4,10,8])
    n = [1,1,0,0,1,1,0,1,1,1]
    print()

    # print(''.join([str(i) for i in n]).split('1'))

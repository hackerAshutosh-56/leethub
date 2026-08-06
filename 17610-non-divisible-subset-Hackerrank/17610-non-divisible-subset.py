#!/bin/python3

import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    count = [0] * k

    # Count frequencies of remainders
    for num in s:
        count[num % k] += 1

    # At most one element with remainder 0
    res = min(count[0], 1)

    for i in range(1, k // 2 + 1):
        if i != k - i:
            res += max(count[i], count[k - i])
        else:
            # When k is even and i == k/2
            res += min(count[i], 1)

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna
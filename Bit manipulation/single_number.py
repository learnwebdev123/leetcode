"""
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.

NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
"""

from unittest import result


def solve(A):
    result = 0
    for i in range(0, len(A)):
        result = result ^ A[i]
    return result


output = solve([1, 2, 2, 3, 1])
print(output)
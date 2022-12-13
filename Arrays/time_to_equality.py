"""
Given an integer array A of size N. In one second, you can increase the value of one element by 1.

Find the minimum time in seconds to make all elements of the array equal.
"""

class Solution:

    @staticmethod
    def max_ele(A):
        maxi = A[0]
        for i in A:
            if i > maxi:
                maxi = i
        return maxi

    def solve(self, A):
        seconds = 0
        max_ele = Solution.max_ele(A)
        for i in A:
            diff = max_ele - i
            seconds = seconds + diff
        return seconds


obj = Solution()
print(obj.solve([2,4,1,3,2]))
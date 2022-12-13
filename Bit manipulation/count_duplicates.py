"""
You are given an integer array A having length N. You have to find the number of duplicate(redundant) elements in the array. 
"""

from operator import le


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
     def solve(self, A):
        count = 0
        for i in range(0, len(A)):
            for j in range(i+1, len(A)):
                if A[i] == A[j]:
                    count +=1
                    break
        return count





obj = Solution()
print(obj.solve([1, 10, 20, 1, 25, 1, 10, 30, 25, 1]))
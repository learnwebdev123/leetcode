# """
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.
# Note: Return the two numbers in ascending order.

# """

# class Solution:
#     # @param A : list of integers
#     # @return a list of integers
#     def solve(self, A):

#         #find the xor of all elements and get val
#         val =0
#         for i in range(0,len(A)):
#             val = val^A[i]

#         #find the pos of set and unset
#         pos = -1
#         for i in range(0,31):
#             if Solution.checkbit(val, i):
#                 pos = i
#                 break

#         set_bit, unset_bit = 0,0
#         for i in range(0,len(A)):
#             if Solution.checkbit(A[i], pos):
#                 set_bit = set_bit^A[i]
#             else:
#                 unset_bit = unset_bit^A[i]
#         if unset_bit > set_bit:
#             return [set_bit, unset_bit]
#         return [unset_bit, set_bit]


#     #find pos of set and unset using checkbit
#     @staticmethod
#     def checkbit(num, i):
#         if (num >> i) & 1 == 1:
#             return True
#         return False


# obj = Solution()
# result = obj.solve([1, 2, 3, 1, 2, 4])
# print(result)

print(-40%7)
# """
# Write a function that takes an integer and returns the number of 1 bits it has.
# """
# def solve(num):
#     count = 0
#     while num>0:
#         if num & 1 == 1:
#             count +=1
#         num = num >>1
#         return count


# result = solve(10)
# print(result)


# """
# Write a function that takes an integer and pos and returns if the pos is set or unset.
# """

# def solve(A,i):
#     if (A >>i) & 1 == 0:
#         print('unset')
#     else:
#         print('set')

# solve(10,2)
    

# """
# Write a function that takes an integer and returns count of set bits.
# """

def solve(num):
    count = 0
    while num:
        if num & 1 == 1:
            count +=1
        num = num >> 1
    return count

print(solve(10))
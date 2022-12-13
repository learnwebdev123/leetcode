class Solution:

    def solve(self, a,b):
        for i in range(0,len(a)-1):
            for j in range(i+1,len(a)):
                if (a[i]+a[j] == b):
                    return True
        return False


obj = Solution()
print(obj.solve(1,2,3,4),7)
class Solution:
    
    def solve(self,a ,b):
        n = len(a)
        for i in range(0, n-1):
            for j in range(i+1,n):
                if(a[i]+a[j] == b):
                    return True
        return False

obj = Solution()
print(obj.solve([1,2,3,4],7))
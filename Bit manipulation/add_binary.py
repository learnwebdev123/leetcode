def addBinary(self, a: str, b: str) -> str:
        mini = min(len(a), len(b))
        maxi = max(len(a), len(b))
        diff = maxi-mini
        ans = ''
        if diff>0:
            if len(a)>len(b):
                b = '0'*diff+''+b
            else:
                a = '0'*diff+''+a
        
        carry = 0
        sm =0
        while maxi>0:
            sm = (int(a[maxi-1]) + int(b[maxi-1])+carry)
            digit = sm%2
            carry = sm//2
            ans = str(digit)+''+ans
            maxi = maxi-1
        if carry==1:
            ans = str(carry)+''+ans
        return ans
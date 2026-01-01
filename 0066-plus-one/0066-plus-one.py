class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)
        a=0
        for i in range(n-1,-1,-1):
            m=n-i-1
            a+=(10**i)*digits[m]
        a+=1
        a=str(a)
        ans=[]
        for i in a:
            ans.append(int(i))
        return ans
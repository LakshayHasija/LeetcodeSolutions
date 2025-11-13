class Solution:
    def maxOperations(self, s: str) -> int:
        ones=[]
        ans=0
        for i in range(len(s)):
            if s[i]=='1':
                ones.append(i)
            else:
                if i>0 and s[i-1]=='0':
                    continue
                ans+=len(ones)
        print(ones)
        return ans
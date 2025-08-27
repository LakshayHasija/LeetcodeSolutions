class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(s)<k:
            return s[::-1]
        ans=[]
        rev=False
        i=0
        temp=[]
        while i<=len(s):
            if i%k==0:
                if rev:
                    ans.extend(temp[::-1])
                else:
                    ans.extend(temp)
                temp=[]
                rev=not rev
            if i==len(s):
                if rev:
                    ans.extend(temp[::-1])
                else:
                    ans.extend(temp)
                break
            temp.append(s[i])
            i+=1
        return "".join(ans)
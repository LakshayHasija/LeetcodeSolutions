class Solution:
    def processStr(self, s: str) -> str:
        ans=[]
        for i in range(len(s)):
            if s[i]=="#":
                ans*=2
            elif s[i]=="*":
                if len(ans)>0:
                    ans.pop()
            elif s[i]=="%":
                ans.reverse()
            else:
                ans.append(s[i])
        return "".join(ans)
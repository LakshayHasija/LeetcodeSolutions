class Solution:
    def smallestPalindrome(self, s: str) -> str:
        first=[]
        for i in range(len(s)//2):
            first.append(s[i])
        first.sort()
        if len(s)%2==0:
            return "".join(first+first[::-1])
        ans=first+[s[len(s)//2]]+first[::-1]
        return "".join(ans)
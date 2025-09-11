class Solution:
    def sortVowels(self, s: str) -> str:
        vowels='aeiou'
        toswap=[]
        index=[]
        ans=[]
        for i in range(len(s)):
            ans.append(s[i])
            if s[i].lower() in vowels:
                toswap.append(s[i])
                index.append(i)
        toswap.sort()
        for i in range(len(index)):
            ans[index[i]]=toswap[i]
        return ''.join(ans)
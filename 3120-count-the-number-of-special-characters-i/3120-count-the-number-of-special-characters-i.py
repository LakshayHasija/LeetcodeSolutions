class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower=set()
        upper=set()
        ans=0
        for i in range(len(word)):
            if ord(word[i])>95: #lower
                if word[i] in lower:
                    continue
                lower.add(word[i])
                if word[i].upper() in upper:
                    ans+=1
            else:
                if word[i] in upper:
                    continue
                upper.add(word[i])
                if word[i].lower() in lower:
                    ans+=1
        return ans
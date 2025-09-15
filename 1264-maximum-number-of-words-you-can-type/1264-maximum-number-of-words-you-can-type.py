class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        s_text=text.split()
        count=0
        for i in s_text:
            for j in i:
                if j in brokenLetters:
                    count+=1
                    break
        return len(s_text)-count
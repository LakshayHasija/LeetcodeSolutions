class Solution:
    def minimumPushes(self, word: str) -> int:
        savednum=0
        keymap={}
        ans=0
        for i in range(len(word)):
            if not word[i] in keymap:
                val=savednum//8
                keymap[word[i]]=val+1
                savednum+=1
        for i in range(len(word)):
             ans+=keymap[word[i]]
        return ans
class Solution:
    def minInsertions(self, word1: str) -> int:
        word2=word1[::-1]
        n=len(word1)
        curr=[0 for i in range(n+1)]
        prev=[0 for i in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(curr[j-1],prev[j])
            prev,curr=curr,[0 for i in range(n+1)]
        return n-prev[n]
        
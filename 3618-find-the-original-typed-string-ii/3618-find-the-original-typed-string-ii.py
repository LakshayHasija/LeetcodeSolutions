class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod=10**9+7
        if not word:
            return 0
        if len(word)==k:
            return 1
        freq=Counter(word)
        diff=len(word)-k
        count=1
        freq={k:v for k,v in freq.items() if v > 1}
        if k<=len(freq):
            for i in freq.values():
                count*=i
            return count%mod
        dp=[0]*k
        dp[0]=1
        for i in freq.values():
            newdp=[0]*k
            sum_=0
            for j in range(k):
                if j>0:
                    sum_=(sum_+dp[j-1])%mod
                if j>i:
                    sum_=(sum_-dp[j-i-1])
                newdp[j]=sum_
            dp=newdp
        invalid_records=sum(dp[len(freq):k])%mod
        return (count-invalid_records)%mod
        

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq=Counter(nums)
        res=freq[1]-(freq[1]%2==0)
        for key in freq:
            print(key)
            k=0
            while key>1:
                if freq[key]>1:
                    k+=2
                    key*=key
                if freq[key]==1:
                    k+=1
                    break
                if freq[key]==0:
                    k-=1
                    break
            res=max(res,k)
        return res
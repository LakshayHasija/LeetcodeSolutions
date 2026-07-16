class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        max_num=0
        prefix_gcd=[]
        for i in nums:
            if i>max_num:
                max_num=i
            prefix_gcd.append(gcd(i,max_num))
        prefix_gcd.sort()
        i=0
        j=len(prefix_gcd)-1
        ans=0
        while i<j:
            ans+=gcd(prefix_gcd[i],prefix_gcd[j])
            i+=1
            j-=1
        return ans
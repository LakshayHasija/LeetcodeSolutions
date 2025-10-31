class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        set_=set()
        ans=[]
        for i in nums:
            if len(ans)==2:
                break
            if i in set_:
                ans.append(i)
            set_.add(i)
        return ans
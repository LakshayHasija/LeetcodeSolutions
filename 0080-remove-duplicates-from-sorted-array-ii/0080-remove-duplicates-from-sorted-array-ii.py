class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a=defaultdict(int)
        k=0
        i=0
        while i<len(nums):
            k+=1
            a[nums[i]]+=1
            if a[nums[i]]>2:
                nums.pop(i)
                k-=1
            else:
                i+=1
        return k
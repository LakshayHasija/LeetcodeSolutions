class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        remove=[]
        for i in range(n-1):
            if nums[i]==nums[i+1]:
                remove.append(i)
        k=n-len(remove)
        for i in remove[::-1]:
            nums.pop(i)
        return k
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nums.sort()
        missing=[]
        count=1
        i=0
        n=len(nums)
        while count<=n and i<n:
            if nums[i]==count:
                i+=1
                count+=1
            elif nums[i]<count:
                i+=1
            else:
                missing.append(count)
                count+=1
        while count<=n:
            missing.append(count)
            count+=1
        return missing
class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums_ind=[(num,i) for i,num in enumerate(nums)]
        nums_ind.sort(key=lambda x:-x[0])
        top_k=sorted(nums_ind[:k],key=lambda x:x[1])
        return [i for i,j in top_k]
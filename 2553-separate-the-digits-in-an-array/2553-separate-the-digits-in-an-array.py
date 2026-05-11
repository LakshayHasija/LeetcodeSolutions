class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in nums:
            n=str(i)
            for j in n:
                answer.append(int(j))
        return answer
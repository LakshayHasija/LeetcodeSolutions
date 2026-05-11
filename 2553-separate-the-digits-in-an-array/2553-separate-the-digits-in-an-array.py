class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer=[]
        for i in nums:
            temp=[]
            while i%10!=i:
                n=i%10
                i=i//10
                temp.append(n)
            temp.append(i)
            answer.extend(temp[::-1])
        return answer
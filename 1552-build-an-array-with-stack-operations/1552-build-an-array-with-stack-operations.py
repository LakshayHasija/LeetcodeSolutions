class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        temp=1
        for i in target:
            while i!=temp:
                stack.append('Push')
                stack.append('Pop')
                temp+=1
            stack.append('Push')
            temp+=1
        return stack
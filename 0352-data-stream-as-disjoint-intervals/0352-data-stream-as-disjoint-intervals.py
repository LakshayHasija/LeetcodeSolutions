#BRUTE FORCE
class SummaryRanges:

    def __init__(self):
        self.arr=[]

    def addNum(self, value: int) -> None:
        self.arr.append(value)
        

    def getIntervals(self) -> List[List[int]]:
        if not self.arr:
            return []
        self.arr.sort()
        stack=[self.arr[0]]
        ans=[]
        for i in range(1,len(self.arr)):
            if self.arr[i]==stack[-1]:
                continue
            if self.arr[i]!=stack[-1]+1:
                if len(stack)==1:
                    ans.append([stack[-1],stack[-1]])
                else:
                    ans.append([stack[0],stack[-1]])
                stack=[]
            stack.append(self.arr[i])
        if len(stack)==1:
            ans.append([stack[-1],stack[-1]])
        else:
            ans.append([stack[0],stack[-1]])
        return ans


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
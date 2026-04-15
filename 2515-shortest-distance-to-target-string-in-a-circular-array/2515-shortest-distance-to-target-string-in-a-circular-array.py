class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        if target not in words: 
            return -1
        if target==words[startIndex]: 
            return 0
        count1=0
        for i in range(startIndex, n + startIndex):
            count1+=1
            if words[(i+1)%n]==target:
                break
        count2=0
        for i in range(startIndex,-n,-1):
            count2+=1
            if words[((i-1)+n)%n]==target:
                break
        return min(count1,count2)
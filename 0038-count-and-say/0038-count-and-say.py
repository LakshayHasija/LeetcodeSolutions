class Solution:
    def countAndSay(self, n: int) -> str:
        current="1"
        for _ in range(n - 1):
            next_term=""
            count=1
            for i in range(len(current)):
                if i+1<len(current) and current[i]==current[i + 1]:
                    count+=1
                else:
                    next_term+=str(count)+current[i]
                    count=1
            current=next_term
        return current
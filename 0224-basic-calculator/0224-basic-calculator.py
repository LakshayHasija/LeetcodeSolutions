class Solution:
    def calculate(self, s: str) -> int:
        stack=[]
        l1=[]
        for i in range(len(s)):
            if s[i]==" ":
                continue
            l1.append(s[i])
        i=0
        while i<len(l1):
            if l1[i]=="(":
                stack.append(i)
            if l1[i]==")":
                t=stack.pop()
                l1=l1[:t]+[str(eval("".join(l1[t+1:i])))]+l1[i+1:]
                # print(l1)
                i=t
            i+=1
        return eval("".join(l1))
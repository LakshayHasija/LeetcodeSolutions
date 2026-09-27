class Solution:
    def reverse(self,str):
        return str[::-1]
    def reverseParentheses(self, s: str) -> str:
        stack=[]        #index for opening bracket
        for i in range(len(s)):
            if s[i]=="(":
                stack.append(i)
            if s[i]==")":
                k=stack.pop()
                s=s[:k]+self.reverse(s[k:i])+s[i:]
        return s.replace("(","").replace(")","")
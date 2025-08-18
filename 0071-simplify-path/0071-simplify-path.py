class Solution:
    def simplifyPath(self, path: str) -> str:
        # .           - current directory
        # ..          - prev
        # /  //  ///  - single /
        stack=[]
        directories=path.split("/")
        for i in directories:
            if i=="":
                continue
            if i==".":
                continue
            if i=="..":
                if stack:
                    stack.pop()
                continue
            stack.append(i)
        return "/"+"/".join(stack)

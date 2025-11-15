class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack=[]
        ans=[0]*n
        for i in logs:
            id,val,time=i.split(':')
            if val=='end':
                d,v,t=stack.pop()
                ans[int(id)]+=(int(time)-int(t)+1)
                if stack:
                    ans[int(stack[-1][0])]-=(int(time)-int(t)+1)
            else:
                stack.append((id,val,time))
        return ans
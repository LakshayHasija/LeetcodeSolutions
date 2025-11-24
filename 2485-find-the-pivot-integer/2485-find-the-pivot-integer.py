class Solution:
    def pivotInteger(self, n: int) -> int:
        if n==1:
            return 1
        elif n==2:
            return -1
        else:
            l=[]
            for i in range(1,n+1):
                l.append(i)
            l=l[-1::-1]
            for i in range(n):
                if sum(l[:i+1]) == sum(l[i:]):
                    print(l[:i+1],l[i:])
                    return l[i]
            return -1
class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        memo={}
        def solve(X,Y):
            key=X+Y
            if key in memo:
                return memo[key]
            if X==Y:
                memo[key]=True
                return memo[key]
            if len(X)<=1:
                memo[key]=False
                return memo[key]
            n=len(X)
            flag=False
            for k in range(n):
                #swap
                for k in range(1,n):
                    if solve(X[:k],Y[n-k:]) and solve(X[k:],Y[:n-k]):
                        flag=True
                        break
                    #no swap
                    if solve(X[:k],Y[:k]) and solve(X[k:],Y[k:]):
                        flag=True
                        break
            memo[key]=flag
            return memo[key]
        return solve(s1,s2)
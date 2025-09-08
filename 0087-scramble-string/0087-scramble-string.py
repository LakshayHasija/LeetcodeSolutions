class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def solve(X,Y):
            if X==Y:
                return True
            if len(X)<=1:
                return False
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
            return flag
        return solve(s1,s2)
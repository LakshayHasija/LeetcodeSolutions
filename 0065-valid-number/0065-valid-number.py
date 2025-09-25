class Solution:
    def isNumber(self, s: str) -> bool:
        invalids=['i','I','n','N']
        for i in invalids:
            if i in s:
                return False
        try:
            p=float(s)
            return True
        except:
            return False
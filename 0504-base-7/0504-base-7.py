class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return "0"
        sign=""
        if num<0:
            sign="-"
            num=abs(num)
        res=""
        while num>0:
            a=num%7
            num=num//7
            res=str(a)+res
        return sign+res
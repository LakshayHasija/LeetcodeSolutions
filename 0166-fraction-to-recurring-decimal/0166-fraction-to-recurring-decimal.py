class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator==0:
            return "0"
        temp=numerator/denominator
        ans=[]
        if (numerator<0) ^ (denominator<0):
            ans.append('-')
        numerator,denominator=abs(numerator),abs(denominator)
        ans.append(str(numerator//denominator))
        remainder=numerator%denominator
        if remainder==0:
            return ''.join(ans)
        ans.append('.')
        decimals=[]
        remainder_pos={}
        while remainder!=0:
            if remainder in remainder_pos:
                idx=remainder_pos[remainder]
                decimals.insert(idx,'(')
                decimals.append(')')
                break
            remainder_pos[remainder]=len(decimals)
            remainder*=10
            digit=remainder//denominator
            decimals.append(str(digit))
            remainder%=denominator
        return ''.join(ans)+''.join(decimals)
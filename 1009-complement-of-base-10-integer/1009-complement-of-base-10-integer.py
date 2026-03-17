class Solution:
    def bitwiseComplement(self, n: int) -> int:
        l=""
        s=bin(n)[2:]
        for i in s:
            if i=='0':
                l+='1'
            else:
                l+='0'
        return int(l, 2)
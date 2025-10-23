class Solution:
    def hasSameDigits(self, s: str) -> bool:
        while len(s)>2:
            nums=[]
            for i in range(1,len(s)):
                nums.append(str((int(s[i-1])+int(s[i]))%10))
            s=''.join(nums)
        return s[0]==s[1]
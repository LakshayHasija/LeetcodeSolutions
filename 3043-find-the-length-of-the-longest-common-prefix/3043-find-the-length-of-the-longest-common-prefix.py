#brute force
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes=set()
        for num in arr1:
            x=num
            while x>0:
                prefixes.add(x)
                x//=10
        ans=0
        for num in arr2:
            x=num
            while x>0:
                if x in prefixes:
                    ans=max(ans,len(str(x)))
                    break
                x//=10
        return ans
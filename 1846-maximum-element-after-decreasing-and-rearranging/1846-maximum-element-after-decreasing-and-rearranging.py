class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        #BRUTE FORCE
        # arr.sort()
        # i,n=1,len(arr)
        # arr[0]=1
        # while i<n:
        #     while abs(arr[i]-arr[i-1])>1:
        #         arr[i]-=1
        #     i+=1
        # return max(arr)
        arr.sort()
        i,n=1,len(arr)
        arr[0]=1
        while i<n:
            if arr[i]>arr[i-1]:
                arr[i]=arr[i-1]+1
            else:
                arr[i]=arr[i-1]
            i+=1
        return arr[-1]
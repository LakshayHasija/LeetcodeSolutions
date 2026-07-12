class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        if not arr:
            return []
        ranked_arr={}
        sorted_arr=sorted(arr)
        i=1
        ranked_arr[sorted_arr[0]]=1
        while i<len(arr):
            if sorted_arr[i]!=sorted_arr[i-1]:
                ranked_arr[sorted_arr[i]]=ranked_arr[sorted_arr[i-1]]+1
            i+=1
        ans=[]
        for i in arr:
            ans.append(ranked_arr[i])
        return ans
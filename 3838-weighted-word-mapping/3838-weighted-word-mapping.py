class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        # print(ord("a"),ord("z"))
        ans=''
        alphanum={}
        for i in range(97,123):
            alphanum[123-i]=[weights[i-97],chr(i)]
        # print(alphanum)
        for i in words:
            sum_=0
            for j in i:
                sum_+=alphanum[123-ord(j)][0]
                # print(j,alphanum[123-ord(j)][0])
            # print(sum_)
            ans+=alphanum[sum_%26+1][1]
        return ans
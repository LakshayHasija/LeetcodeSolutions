class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ##BRUTE FORCE##
        # ans=[0]*len(spells)
        # for i in range(len(spells)):
        #     for j in potions:
        #         if spells[i]*j>=success:
        #             ans[i]+=1
        # return ans
        potionsSuccess=[]
        potions.sort()
        for i in potions:
            potionsSuccess.append(success//i) if success%i==0 else potionsSuccess.append((success//i)+1)
        # print(potionsSuccess)
        ans=[0]*len(spells)
        for i in range(len(spells)):
            #This is working but still getting a TLE, so for this part I thought of using Binary Search
            # j=0
            # while j<len(potions) and potionsSuccess[j]>spells[i]:
            #     j+=1
            # ans[i]=len(potions)-j
            l=0
            r=len(potionsSuccess)-1
            if potionsSuccess[r]>spells[i]:
                ans[i]=0
                continue
            while l<r:
                mid=(l+r)//2
                if potionsSuccess[mid]>spells[i]:
                    l=mid+1
                else:
                    r=mid
            ans[i]=len(potionsSuccess)-r
        return ans
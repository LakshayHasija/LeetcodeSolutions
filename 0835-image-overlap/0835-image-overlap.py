class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        pos1=[]
        pos2=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    pos1.append((i,j))
                if img2[i][j]==1:
                    pos2.append((i,j))
        track=defaultdict(int)
        ans=0
        for i,j in pos1:
            for x,y in pos2:
                track[(i-x,j-y)]+=1
                if track[(i-x,j-y)]>ans:
                    ans=track[(i-x,j-y)]
        return ans
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        temp=copy.deepcopy(mat)
        n=len(temp[0])
        k=k%n
        for i in range(len(temp)):
            if i%2==0:
                for _ in range(k):
                    temp[i].append(temp[i][0])
                    temp[i].pop(0)
            else:
                for _ in range(k):
                    m=temp[i].pop()
                    temp[i].insert(0,m)
        return temp==mat
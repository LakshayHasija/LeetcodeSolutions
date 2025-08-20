class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        if label==1:
            return [1]
        node=0
        for i in range(1,100):
            prev=node
            node=2**i-1
            if node>=label:
                break
        print(prev,node)
        label1=prev+node-label+1
        l1or=[label1]
        lor=[label]
        print(label1)
        while True:
            if lor[-1]==2 or lor[-1]==3:
                lor.append(1)
                l1or.append(1)
                break
            lor.append(lor[-1]//2)
            l1or.append(l1or[-1]//2)
        ans=[]
        for i in range(len(lor)-1,-1,-1):
            if i%2==0:
                ans.append(lor[i])
            else:
                ans.append(l1or[i])
        return ans
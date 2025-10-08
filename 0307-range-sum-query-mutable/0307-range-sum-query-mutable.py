class NumArray:

    def __init__(self, arr: List[int]):
        self.n=len(arr)
        self.st=[0]*(4*self.n)
        def buildTree(i,l,r):
            if l==r:
                self.st[i]=arr[l]
                return arr[l]
            mid=(l+r)//2
            left=buildTree(2*i+1,l,mid)
            right=buildTree(2*i+2,mid+1,r)
            self.st[i]=left+right
            return self.st[i]
        buildTree(0,0,self.n-1)
        
    def update(self, index: int, val: int) -> None:
        def helper(i,l,r):
            if l==r:
                self.st[i]=val
                return
            mid=(l+r)//2
            if index<=mid:
                helper(2*i+1,l,mid)
            else:
                helper(2*i+2,mid+1,r)
            self.st[i]=self.st[2*i+1]+self.st[2*i+2]
        helper(0,0,self.n-1)

    def sumRange(self, left: int, right: int) -> int:
        def helper(i,l,r):
            if left<=l and r<=right:
                return self.st[i]
            if r<left or l>right:
                return 0
            mid=(l+r)//2
            return helper(2*i+1,l,mid) + helper(2*i+2,mid+1,r)
        return helper(0,0,self.n-1)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
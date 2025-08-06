# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        curr=head
        q=deque()
        while curr:
            q.append(curr.val)
            curr=curr.next
        ans=[]
        for i in range(m):
            temp=[-1]*n
            ans.append(temp)
        i=0
        j=-1
        l,b=1,0
        increasing=True
        while q:
            if increasing:
                j+=1
                while q and j<n:
                    ans[i][j]=q.popleft()
                    j+=1
                j-=1
                i+=1
                while q and i<m:
                    ans[i][j]=q.popleft()
                    i+=1
                i-=1
                increasing=False
                m-=1
                n-=1
            if not increasing:
                j-=1
                while q and j>=b:
                    ans[i][j]=q.popleft()
                    j-=1
                j+=1
                i-=1
                while q and i>=l:
                    ans[i][j]=q.popleft()
                    i-=1
                i+=1
                increasing=True
                l+=1
                b+=1
        return ans
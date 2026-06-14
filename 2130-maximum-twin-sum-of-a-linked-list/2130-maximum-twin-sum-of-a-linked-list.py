# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        linkedlist=[]
        curr=head
        while curr:
            linkedlist.append(curr.val)
            curr=curr.next
        n=len(linkedlist)
        m=n//2
        i=0
        ans=0
        while i<m:
            ans=max(linkedlist[i]+linkedlist[n-1-i],ans)
            i+=1
        return ans
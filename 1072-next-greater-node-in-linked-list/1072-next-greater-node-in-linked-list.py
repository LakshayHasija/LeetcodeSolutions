# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        reverse=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return reverse
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        head1=self.reverseList(head)
        stack=[]
        ans=[]
        curr=head1
        while curr:
            while stack and stack[-1]<=curr.val:
                stack.pop()
            if stack:
                ans.append(stack[-1])
            else:
                ans.append(0)
            stack.append(curr.val)
            curr=curr.next
        return ans[::-1]
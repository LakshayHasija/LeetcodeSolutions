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
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        carry=0
        reverse=self.reverseList(head)
        curr=reverse
        while curr:
            temp=curr.val*2+carry
            curr.val=temp%10
            carry=temp//10
            prev=curr
            curr=curr.next
        if carry!=0:
            node=ListNode(carry)
            prev.next=node
        return self.reverseList(reverse)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverselinkedlist(self,head): 
        prev = None
        curr = head
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr
            curr = next_node
        return prev  
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        head = self.reverselinkedlist(head)
        curr = head
        maxnum = curr.val
        while curr and curr.next:
            if curr.next.val < maxnum:
                curr.next = curr.next.next  
            else:
                curr = curr.next
                maxnum = curr.val
        head = self.reverselinkedlist(head)
        return head
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        prev = head
        curr = head.next
        pos = 1
        first_cp = -1
        last_cp = -1
        prev_cp = -1
        min_dist = float('inf')
        while curr.next:
            next_ = curr.next
            if (curr.val > prev.val and curr.val > next_.val) or (curr.val < prev.val and curr.val < next_.val):
                if first_cp == -1:
                    first_cp = pos
                else:
                    min_dist = min(min_dist, pos - prev_cp)
                prev_cp = pos
                last_cp = pos
            prev = curr
            curr = next_
            pos += 1
        if first_cp == last_cp:
            return [-1, -1]
        return [min_dist, last_cp - first_cp]

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow = head
        fast = head

        # 1. Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, cur, nxt = None, slow.next, None
        slow.next = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 3. Merge both halves
        l1 = head
        l2 = prev

        while l2:
            tmp1, tmp2 = l1.next, l2.next

            l1.next = l2
            l2.next = tmp1

            l1, l2 = tmp1, tmp2
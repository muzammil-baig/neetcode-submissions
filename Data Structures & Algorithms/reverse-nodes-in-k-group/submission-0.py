
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head

        # Count total nodes
        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while count >= k:

            tempCur = groupPrev.next
            tempPrev = None
            tempNxt = None

            # Reverse exactly k nodes
            for i in range(k):
                tempNxt = tempCur.next
                tempCur.next = tempPrev
                tempPrev = tempCur
                tempCur = tempNxt

            # Connect the reversed group
            groupStart = groupPrev.next
            groupPrev.next = tempPrev
            groupStart.next = tempCur

            # Move to the next group
            groupPrev = groupStart

            count -= k

        return dummy.next

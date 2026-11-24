
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or k == 1:
            return head

        count = 0
        cur = head
        while cur:
            count += 1
            cur = cur.next

        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy

        while count >= k:
            tempCur, tempPrev, tempNext = groupPrev.next, None, None

            for i in range(k):
                tempNext = tempCur.next
                tempCur.next = tempPrev
                tempPrev = tempCur
                tempCur = tempNext

            groupStart = groupPrev.next
            groupPrev.next = tempPrev
            groupStart.next = tempCur

            groupPrev = groupStart

            count -= k

        return dummy.next
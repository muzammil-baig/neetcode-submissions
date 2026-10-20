# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None
        if head.next == None and n == 1:
            return None
        cur = head
        temp = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        loop = count - n - 1

        if n == count:
            return head.next

        for i in range(loop):
            temp = temp.next

        nextNode = temp.next.next

        temp.next = nextNode
        return head

        
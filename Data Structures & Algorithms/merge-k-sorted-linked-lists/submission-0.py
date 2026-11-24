# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode(0)
        l1 = []
        for node in lists:
            while node:
                l1.append(node.val)
                node = node.next
        l1.sort()
        if not l1:
            return None
        one = ListNode(l1[0])
        dummy.next = one
        curr = dummy.next

        for i in range(1, len(l1)):
            newNode = ListNode(l1[i])
            curr.next = newNode
            curr = curr.next

        return dummy.next

            
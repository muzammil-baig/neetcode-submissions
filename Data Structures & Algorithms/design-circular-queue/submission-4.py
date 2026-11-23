class ListNode:
    def __init__(self, val, prev, nxt):
        self.val = val 
        self.prev = prev
        self.nxt = nxt

class MyCircularQueue:

    def __init__(self, k: int):
        self.space = k
        self.left = ListNode(0, None, None)
        self.ryt = ListNode(0, self.left, None)
        self.left.nxt = self.ryt

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        cur = ListNode(value, self.ryt.prev, self.ryt)
        self.ryt.prev.nxt = cur
        self.ryt.prev = cur
        self.space -= 1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        cur = self.left.nxt
        self.left.nxt = cur.nxt
        cur.nxt.prev = self.left
        self.space += 1
        return True

    def Front(self) -> int:
        if self.isEmpty():
            return -1
        return self.left.nxt.val

    def Rear(self) -> int:
        if self.isEmpty():
            return -1
        return self.ryt.prev.val

    def isEmpty(self) -> bool:
        return self.left.nxt == self.ryt

    def isFull(self) -> bool:
        return self.space == 0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
class StockSpanner:

    def __init__(self):
        self.s1 = []

    def next(self, price: int) -> int:
        self.s1.append(price)

        count = 1
        j = len(self.s1) - 2

        while j >= 0 and self.s1[j] <= price:
            count += 1
            j -= 1
        
        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
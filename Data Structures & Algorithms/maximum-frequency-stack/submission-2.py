class FreqStack:

    def __init__(self):
        self.hM = {}       # value -> frequency
        self.count = {}    # frequency -> stack of values
        self.maxFreq = 0

    def push(self, val: int) -> None:
        freq = 1 + self.hM.get(val, 0)
        self.hM[val] = freq

        if freq not in self.count:
            self.count[freq] = []

        self.count[freq].append(val)

        self.maxFreq = max(self.maxFreq, freq)

    def pop(self) -> int:
        val = self.count[self.maxFreq].pop()

        self.hM[val] -= 1

        if not self.count[self.maxFreq]:
            self.maxFreq -= 1

        return val
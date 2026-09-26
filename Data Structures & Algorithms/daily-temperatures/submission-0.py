class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for i, a in enumerate(temperatures):
            while stack and a > stack[-1][0]:
                prevVal, prevIndx = stack.pop()
                res[prevIndx] = i - prevIndx
        
            stack.append((a, i))

        return res
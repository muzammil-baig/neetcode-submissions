class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for i in range(len(operations)):
            if operations[i].lstrip("-").isdigit():
                stack.append(int(operations[i]))
            elif operations[i] == "+":
                if len(stack) < 2:
                    continue
                res = stack[-1] + stack[-2]
                stack.append(res)
            elif operations[i] == "C":
                if not stack:
                    continue
                stack.pop()
            elif operations[i] == "D":
                if len(stack) < 1:
                    continue
                res = stack[-1] * 2
                stack.append(res)
        
        return sum(stack)
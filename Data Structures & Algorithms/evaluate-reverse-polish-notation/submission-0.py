class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s1 = []
        for s in tokens:
            if s == "+":
                val1 = s1.pop()
                val2 = s1.pop()
                res = val1 + val2
                s1.append(res)
            elif s == "*":
                val1 = s1.pop()
                val2 = s1.pop()
                res = val1 * val2
                s1.append(res)
            elif s == "-":
                if len(s1) < 2:
                    continue
                val1 = s1.pop()
                val2 = s1.pop()
                res = val2 - val1
                s1.append(res)
            elif s == "/":
                val1 = s1.pop()
                val2 = s1.pop()
                res = int(val2 / val1)
                s1.append(res)  
            else:
                s1.append(int(s))

        return s1[-1] 
class Solution:
    def isValid(self, s: str) -> bool:
        hM = {"}":"{", "]": "[", ")": "("}
        stack = []

        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] != hM[i]:
                    return False
                stack.pop()

        return len(stack) == 0
        
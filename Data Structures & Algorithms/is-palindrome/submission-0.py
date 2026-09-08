class Solution:
    def isPalindrome(self, s: str) -> bool:
        m = ""
        for i in s:
            if i.isalnum():
                m += i
            
        print(m)
        r = m.lower()
        print(r)
        p1 = 0
        p2 = len(r) - 1
        while p1 < p2:
            if r[p1] != r[p2]:
                return False
            p1 += 1
            p2 -= 1

        return True
        
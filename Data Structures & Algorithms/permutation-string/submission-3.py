class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        res, l = 0, 0
        count = {}
        count2 = {}
        for i in range(len(s1)):
            count2[s1[i]] = 1 + count2.get(s1[i], 0)
        for r in range(len(s2)):
            count[s2[r]] = 1 + count.get(s2[r], 0)
            if r - l + 1 > len(s1):
                count[s2[l]] -= 1

                if count[s2[l]] == 0:
                    del count[s2[l]]
                
                l += 1

            if count == count2:
                return True
        return False

            

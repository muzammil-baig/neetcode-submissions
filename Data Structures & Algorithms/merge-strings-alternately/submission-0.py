class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = word1 + word2
        r = ""

        p1 = 0
        p2 = len(word1)

        for i in range(len(merge)):
            if i % 2 == 0:
                if p1 < len(word1):
                    r += merge[p1]
                    p1 += 1
                else:
                    r += merge[p2]
                    p2 += 1

            else:
                if p2 < len(merge):
                    r += merge[p2]
                    p2 += 1
                else:
                    r += merge[p1]
                    p1 += 1

        return r

        
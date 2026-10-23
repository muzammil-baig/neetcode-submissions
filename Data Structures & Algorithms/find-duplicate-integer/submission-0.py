class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hM = {}

        for n  in nums:
            hM[n] = 1 + hM.get(n, 0)

        for key, val in hM.items():
            if val > 1:
                return key
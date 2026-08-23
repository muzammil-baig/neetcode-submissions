class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        hM = {}
        for n in nums:
            hM[n] = 1 + hM.get(n, 0)
        print(hM)
        t = 0
        for i in range(1, len(nums) + 2):
            if i not in hM:
                return i

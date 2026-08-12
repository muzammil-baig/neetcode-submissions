class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hM = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hM:
                return [hM[val], i]
            hM[nums[i]] = i
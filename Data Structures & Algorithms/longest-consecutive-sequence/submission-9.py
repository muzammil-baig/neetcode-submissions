class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return 1
        maxx = 1
        nums.sort()
        print(nums)
        check = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1] + 1:
                    check += 1
                else:
                    maxx = max(maxx, check)
                    check = 1
        return max(maxx, check)
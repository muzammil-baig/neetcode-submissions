class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        def getPermuate(nums, idx):
            if idx == len(nums):
                check = nums[:]
                if check not in res:
                    res.append(check)
                    return 

            for i in range(idx, len(nums)):
                nums[idx], nums[i] = nums[i], nums[idx]
                getPermuate(nums, idx + 1)
                nums[idx], nums[i] = nums[i], nums[idx]

        getPermuate(nums, 0)
        return res

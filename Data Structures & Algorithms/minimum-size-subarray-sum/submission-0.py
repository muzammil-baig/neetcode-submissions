class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        l,t = 0, 0

        for r in range(len(nums)):
            t += nums[r]
            while t >= target:
                res = min(res, r - l + 1)
                t -= nums[l]
                l += 1

        return 0 if res == float('inf') else res


        
        
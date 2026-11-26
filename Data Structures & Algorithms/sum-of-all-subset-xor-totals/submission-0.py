class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        res = 0

        def Total(nums, ans, i):
            nonlocal res

            if i == len(nums):
                currXor = 0

                for num in ans:
                    currXor ^= num

                res += currXor
                return

            ans.append(nums[i])
            Total(nums, ans, i + 1)

            ans.pop()
            Total(nums, ans, i + 1)

        Total(nums, [], 0)
        return res
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def printSubset(nums, ans, i):
            if i == len(nums):
                res.append(ans[:])
                return 
            ans.append(nums[i])
            printSubset(nums, ans, i+1)
            ans.pop()
            printSubset(nums, ans, i+1)
        printSubset(nums, [], 0)
        return res
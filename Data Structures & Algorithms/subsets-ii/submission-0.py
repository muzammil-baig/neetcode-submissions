class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = list(set())
        def printSubset(nums, ans, i):
            if i == len(nums):
                subset = sorted(ans[:])
                if subset not in res:
                    res.append(subset)
                return 
            
            ans.append(nums[i])
            printSubset(nums, ans, i+1)

            ans.pop()
            printSubset(nums, ans, i+1)
        printSubset(nums, [], 0)
        return res
        
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        newArr = sorted(set(nums))
        nums[:] = newArr
        return len(nums)

        
        
    
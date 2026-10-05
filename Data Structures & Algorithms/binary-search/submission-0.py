class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySerach(nums, target, l, r):
            if l > r:
                return -1 
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySerach(nums, target, l, mid - 1)
            else:
                return binarySerach(nums, target, mid + 1, r)
        
        return binarySerach(nums, target, 0, len(nums) - 1)
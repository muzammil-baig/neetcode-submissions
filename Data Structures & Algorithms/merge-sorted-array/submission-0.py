class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        dup = nums1[0:m]
        for i in range(n):
            dup.append(nums2[i])
        dup = sorted(dup)
        nums1[:] = dup
        
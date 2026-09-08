class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hM = {}
        for i, n in enumerate(numbers):
            diff = target - n
            if diff in hM:
                return [hM[diff] + 1, i+1]
            hM[n] = i
        
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        hM = defaultdict(int)
        for n in nums:
            hM[n] = 1 + hM.get(n, 0)
        if hM[target] != 0:
            return True
        return False
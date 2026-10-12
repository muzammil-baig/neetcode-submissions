class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lower, upper = 1, max(piles)

        while lower <= upper:
            mid = (lower + upper) // 2
            hrs = 0
            for pile in piles:
                hrs += (pile + mid - 1) // mid
            if hrs > h:
                lower = mid + 1
            else:
                upper = mid - 1


        return lower

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lower = max(weights)
        upper = sum(weights)

        while lower <= upper:
            mid = (lower + upper) // 2
            daysNeeded = 1
            currentLoad = 0

            for w in weights:
                if currentLoad + w > mid:
                    daysNeeded += 1
                    currentLoad = 0

                currentLoad += w
            if daysNeeded > days:
                lower = mid + 1
            else:
                upper = mid - 1

        return lower

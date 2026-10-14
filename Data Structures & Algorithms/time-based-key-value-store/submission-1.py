class TimeMap:

    def __init__(self):
        self.hM = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hM[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hM[key]
        if key not in self.hM:
            return ""

        ans = ""
        low, high = 0, len(arr) - 1

        while low <= high:
            mid = (low + high) // 2

            if arr[mid][0] <= timestamp:
                ans = arr[mid][1]
                low = mid + 1
            else:
                high = mid - 1

        return ans

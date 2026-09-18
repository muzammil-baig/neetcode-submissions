class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(x)
        arr.sort()
        i = arr.index(x)
        print(i)
        l = i - 1
        r = i + 1
        res = []

        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1

            elif (r >= len(arr)):
                res.append(arr[l])
                l -= 1

            elif abs(arr[l] - x) <= abs(arr[r] - x):
                res.append(arr[l])
                l -= 1

            else:
                res.append(arr[r])
                r += 1

        return sorted(res)
        
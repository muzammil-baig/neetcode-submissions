class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count = Counter(nums).most_common(k)
        # r = []
        # for i in range(len(count)):
        #     r.append(count[i][0])
        # return r


        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)

        for key, val in count.items():
            freq[val].append(key)
        r = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                r.append(n)
                if len(r) == k:
                    return r

        
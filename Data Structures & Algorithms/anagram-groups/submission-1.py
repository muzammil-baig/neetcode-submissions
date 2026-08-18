class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #res = defaultdict(list)

        # for s in strs:
        #     count = [0] * 26
        #     for c in s:
        #         count[ord(c) - ord('a')] += 1

        #     res[tuple(count)].append(s)
        
        # return list(res.values())

        res = {}
        for s in strs:
            sort_val = "".join(sorted(s))

            if sort_val in res:
                res[sort_val].append(s)
            else:
                res[sort_val] = [s]

        return list(res.values())

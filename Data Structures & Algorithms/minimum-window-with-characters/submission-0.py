class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        need = Counter(t)

        l, have = 0, 0
        res = ""

        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)

            if s[r] in need and window[s[r]] == need[s[r]]:
                have += 1

            while have == len(need):

                # Save smallest valid window
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]

                # Remove s[l]
                window[s[l]] -= 1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1

                l += 1

        return res

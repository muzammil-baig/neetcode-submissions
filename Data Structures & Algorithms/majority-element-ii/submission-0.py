class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        c1 = None
        c2 = None
        count1 = 0
        count2 = 0
        for n in nums:
            if c1 == n:
                count1 += 1
            elif c2 == n:
                count2 += 1

            elif count1== 0:
                c1 = n
                count1 = 1
            elif count2== 0:
                c2 = n
                count2 = 1

            else:
                count1 -= 1
                count2 -= 1
        ans = []
        count1 = nums.count(c1)
        count2 = nums.count(c2)
        if count1 > len(nums) // 3:
            ans.append(c1)
        if count2 > len(nums) // 3 and c2 != c1:
            ans.append(c2)
        return ans
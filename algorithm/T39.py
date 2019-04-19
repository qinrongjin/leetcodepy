from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = 0
        m = nums[0]
        for n in nums:
            s += n
            print(n, s, m)
            if s > m:
                m = s
            if s < 0:
                s = 0
        return m


ret = Solution().maxSubArray([-3, -2, 0, -1])
print(ret)

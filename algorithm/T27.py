from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0
        for i in range(0, nums.__len__()):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j


result = Solution().removeElement([4, 5, 4, 6, 7, 8, 4], 4)
print(result)

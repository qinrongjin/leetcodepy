from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if (nums.__len__() == 0):
            return 0
        j = 1
        i = 1
        while j < nums.__len__():
            if nums[j] > nums[i - 1]:
                nums[i] = nums[j]
                i += 1
            j += 1
            print(i, j, nums)
        return i


j = Solution().removeDuplicates([])
print(j)

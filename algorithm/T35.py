from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = self.binSearch(nums, target, 0, nums.__len__())
        if nums[mid] >= target:
            return mid
        else:
            return mid + 1

    def binSearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        print(start, end)
        if start >= end - 1:
            return start
        mid = int((start + end) / 2)
        if nums[mid] == target:
            return mid
        if nums[mid] > target:
            return self.binSearch(nums, target, start, mid)
        else:
            return self.binSearch(nums, target, mid, end)
        return


ret = Solution().searchInsert([1, 2, 3, 4, 6, 7, 8, 9], 5)
print(ret)

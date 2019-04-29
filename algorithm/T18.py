from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        l = []
        dic = {}
        for i in range(0, len(nums)):
            dic[target - nums[i]] = i
        print(dic)
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    key = nums[i] + nums[j] + nums[k]
                    value = dic.get(key)
                    if i == 2 and j == 3 and k == 5:
                        print()
                    if value and value != i and value != j and value != k \
                            and value > k:
                        l2 = [nums[i], nums[j], nums[k], nums[value]]
                        if self.notContain(l, l2):
                            l.append(l2)
        return l

    def notContain(self, l1: List[List[int]], l2: List[int]):
        for l in l1:
            temp = l.copy()
            for n in l2:
                if (temp.__contains__(n)):
                    temp.remove(n)
            if temp.__len__() == 0:
                return False
        return True


res = Solution().fourSum([2, -4, -5, -2, -3, -5, 0, 4, -2], -14)
print(res)

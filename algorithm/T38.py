from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        s = self.countAndSay(n - 1)
        if n == 6:
            print()
        return self.convert(s)

    def convert(self, s: str) -> str:
        l1 = []
        l2 = []
        for c in s:
            if len(l1) == 0 or l1[len(l1) - 1] != c:
                l1.append(c)
                l2.append(1)
            else:
                l2[len(l2) - 1] = l2[len(l2) - 1] + 1
        re = ''
        for i in range(0, len(l1)):
            re += str(l2[i])
            re += str(l1[i])
        return re


ret = Solution().countAndSay(6)
print(ret)

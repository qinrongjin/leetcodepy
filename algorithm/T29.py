class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        flag = False
        if dividend < 0:
            dividend = -dividend
            flag = not flag
        if divisor < 0:
            divisor = -divisor
            flag = not flag
        l = []
        ln = []
        s = divisor
        n = 1
        m = 0
        while True:
            if s > dividend:
                break
            l.append(s)
            ln.append(n)
            s = s + s
            n = n + n
        for k in reversed(range(0, l.__len__())):
            if dividend >= l[k]:
                m += ln[k]
                dividend -= l[k]
        return -m if flag else m


a = 14523464
b = -73
ret = Solution().divide(a, b)
print(ret)
print(int(a / b))

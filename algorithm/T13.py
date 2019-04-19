class Solution:
    def romanToInt(self, s: str) -> int:
        l = []
        for c in s:
            n = dic[c]
            l.append(n)
        sum = 0
        for i in range(0, len(l)):
            if i > 0 and l[i] > l[i-1]:
                sum += -2 * l[i-1] + l[i]
            else:
                sum += l[i]
        return sum

dic = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

ret = Solution().romanToInt('IV')
print(ret)
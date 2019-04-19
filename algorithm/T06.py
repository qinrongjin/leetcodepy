class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        period = numRows * 2 - 2
        ret = ''
        for r in range(0, numRows):
            k = r
            m = k % period
            while k < len(s):
                ret += s[k]
                k += period
                if m > 0:
                    n = k - 2 * m
                    if n != k - period and n < len(s):
                        ret += s[n]
        return ret


result = Solution().convert("PAYPALISHIRING", 3)
print(result)




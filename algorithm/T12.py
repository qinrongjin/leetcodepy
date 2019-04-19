class Solution:
    def intToRoman(self, num: int) -> str:
        ne = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        d = {}
        ret = ''
        for n in ne:
            if num >= n:
                k = int(num / n)
                for i in range(0, k):
                    ret += dit[n]
            num = num % n
        return ret


dit = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}

result = Solution().intToRoman(1994)
print(result)

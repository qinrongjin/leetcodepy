class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle.__eq__(''):
            return 0
        first = needle[0]
        for i in range(0, haystack.__len__()):
            if haystack[i] != first:
                print(i, 'continue')
                continue
            cur = i
            l = 0
            for j in range(1, needle.__len__()):
                print(cur, l)
                if cur + j > haystack.__len__() - 1:
                    return -1
                if haystack[cur + j] != needle[j]:
                    break
                l += 1
            print(l, needle.__len__())
            if l == needle.__len__() - 1:
                return cur
        return -1


re = Solution().strStr("a", "a")
print(re)

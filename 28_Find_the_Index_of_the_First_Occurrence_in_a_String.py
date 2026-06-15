class Solution(object):
    def strStr(self, haystack, needle):
        if len(haystack) == 1:
            return 0
        else:
            j = len(needle)-1
            if needle in haystack:
                for i in range(len(haystack)-len(needle)+1):
                    if haystack[i:j+1] == needle:
                        return i
                    else:
                        i += 1
                        j += 1
            return -1

haystack = input()
needle = input()
cls = Solution()
print(cls.strStr(haystack, needle))
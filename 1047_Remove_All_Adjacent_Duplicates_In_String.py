class Solution(object):
    def removeDuplicates(self, s):
        fs = ""
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1

        for j in di:
            if di[j] % 2 != 0:
                fs += j

        if len(fs) == 0:
            return 0
        else:
            return fs

s = input()
cls = Solution()
print(cls.removeDuplicates(s))
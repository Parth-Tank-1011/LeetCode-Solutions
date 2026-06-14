class Solution(object):
    def lengthOfLastWord(self, s):
        count = 0
        s = s.rstrip()
        if len(s) == 1 and s[0] != " ":
            return 1
        else:
            for ch in range(len(s)-1, -1, -1):
                if s[ch] == " ":
                    return count
                else:
                    count += 1
            return count

s = input()
cls = Solution()
print(cls.lengthOfLastWord(s))
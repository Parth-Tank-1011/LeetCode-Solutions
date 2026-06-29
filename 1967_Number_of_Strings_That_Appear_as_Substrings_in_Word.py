class Solution(object):
    def numOfStrings(self, patterns, word):
        count = 0
        for i in patterns:
            if i in word:
                count += 1

        return count
    
patterns = list(map(str, input().split()))
word = input()
cls = Solution()
print(cls.numOfStrings(patterns, word))
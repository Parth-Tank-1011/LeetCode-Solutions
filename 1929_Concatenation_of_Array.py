class Solution(object):
    def getConcatenation(self, nums):
        ans = []
        for i in range(len(nums)):
            ans.append(nums[i])
        #ans.append()
        return ans*2

nums = list(map(int, input().split()))
cls = Solution()
print(cls.getConcatenation(nums))
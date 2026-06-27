class Solution(object):
    def majorityElement(self, nums):
        n = len(nums)/2
        di = {}
        for i in nums:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1

        for j in di:
            if di[j] >= n:
                return j
        else:
            return -1

nums = list(map(int, input().split()))        
cls = Solution()
print(cls.majorityElement(nums))
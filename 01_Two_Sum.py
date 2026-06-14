# Leetcode - 1

class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

nums = list(map(int, input().split()))
target = int(input())

c1 = Solution()
print(c1.twoSum(nums, target))
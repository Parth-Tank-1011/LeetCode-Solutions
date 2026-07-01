##### Brut Force #####

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    if abs(j-i) <= k:
                        return True
        else:
            return False
        
nums = list(map(int, input().split()))
k = int(input())
cls = Solution()
print(cls.containsNearbyDuplicate(nums, k))

##### Optimal #####

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        dic = {}

        for i in range(len(nums)):
            if nums[i] in dic:
                if i - dic[nums[i]] <= k:
                    return True

            dic[nums[i]] = i

        return False


nums = list(map(int, input().split()))
k = int(input())

cls = Solution()
print(cls.containsNearbyDuplicate(nums, k))
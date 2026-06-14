# class Solution(object):
#     def singleNumber(self, nums):
#         temp = {}
#         for i in nums:
#             if i in temp:
#                 temp[i] -= 1
#             else:
#                 temp[i] = 1
        
#         for j in nums:
#             if temp[j] == 1:
#                 return j
            
# nums = list(map(int, input().split()))
# cls = Solution()
# print(cls.singleNumber(nums)) 

##### Optimal Solution #####

class Solution(object):
    def singleNumber(self, nums):
        total = 0
        if len(nums) == 1:
            return nums[0]
        else:
            for i in nums:
                total ^= i
        return total
        
nums = list(map(int, input().split()))
cls = Solution()
print(cls.singleNumber(nums))          
# ##### Brut Force #####

def removeDuplicates(nums):
    ans = []
    ans_len = 0

    for i in range(len(nums)):
        if nums[i] not in ans:
            ans.append(nums[i])
            ans_len += 1
    print(len(ans), end = " ")

    for i in range(len(nums) - len(ans)):
        ans.append("_")
    
    return(f" Nums: {ans}")

nums1 = list(map(int, input().split()))
print(removeDuplicates(nums1))


##### Optimal #####

class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0

        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
    
S = Solution()
user_nums = list(map(int, input().split()))
print(S.removeDuplicates(user_nums))
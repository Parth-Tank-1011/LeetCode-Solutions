# Leetcode - 217

nums = list(map(int, input().split()))

##### Brut Force #####
def containsDuplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
                break
    else:
        return False

print(containsDuplicate(nums))

# ##### Optimal #####

def containsDuplicate(nums):
    temp = set()
    for i in nums:
        if i in temp:
            return True
        else:
            temp.add(i)
    return False
            
print(containsDuplicate(nums))

##### Leatest - Not Recommended #####

def containsDuplicate(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True

print(containsDuplicate(nums))
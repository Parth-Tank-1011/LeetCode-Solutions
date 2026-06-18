##### Brut Force #####

# class Solution(object):
#     def firstUniqChar(self, s):
        
#         for i in range(len(s)):
#             if s[i] not in s[:i] and s[i] not in s[i+1:]:
#                 return i
#         else:
#             return -1
        
# s = input()
# cls = Solution()
# print(cls.firstUniqChar(s))

##### Optimal #####

class Solution(object):
    def firstUniqChar(self, s):
        di = {}
        for i in s:
            if i in di:
                di[i] += 1
            else:
                di[i] = 1

        for i in range(len(s)):
            if di[s[i]] == 1:
                return i
        else:
            return -1
        

        
s = input()
cls = Solution()
print(cls.firstUniqChar(s))
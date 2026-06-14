##### Optimal #####

class Solution(object):
    def isAnagram(self, s, t):
        d1 = {}
        d2 = {}

        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1

        for i in t:
            if i in d2:
                d2[i] += 1
            else:
                d2[i] = 1

        if d1 == d2:
            return True
        else:
            return False
        
s = input()
t = input()
cls = Solution()
print(cls.isAnagram(s, t))

##### Optimal - Not Recommended #####

class Solution(object):
    def isAnagram(self, s, t):

        if sorted(s) == sorted(t):
            return True
        else:
            return False
        
s = input()
t = input()
cls = Solution()
print(cls.isAnagram(s, t))

##### Brut Force #####


def isAnagram(self, s, t):

    for ch in s:
        count1 = 0
        count2 = 0

        for i in s:
            if i == ch:
                count1 += 1

        for i in t:
            if i == ch:
                count2 += 1

        if count1 == count2:
            return True

    return False

s = input()
t = input()
print(isAnagram(s, t))
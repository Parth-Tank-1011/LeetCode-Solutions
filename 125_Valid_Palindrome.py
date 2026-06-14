##### Brut Force #####
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        i = 0
        j = len(s) - 1
        
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum():
                j -= 1
            else:
                if s[i] != s[j]:
                    return False
            
                i += 1
                j -= 1
        
        
        return True


##### Optimal #####

class Solution(object):
    def isPalindrome(self, s):
        s2 = ""

        for ch in s:
            if ch.isalnum():
                s2 += ch.lower()

        return s2 == s2[::-1]

s = input()
cls = Solution
print(cls.isPalindrome(s))        
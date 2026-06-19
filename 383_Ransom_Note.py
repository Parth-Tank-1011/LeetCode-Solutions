class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for ch in ransomNote:
            if ch not in magazine:
                return False
            magazine = magazine.replace(ch, "", 1)
        return True
    
in1 = input()
in2 = input()
cls = Solution()
print(cls.canConstruct(in1, in2))
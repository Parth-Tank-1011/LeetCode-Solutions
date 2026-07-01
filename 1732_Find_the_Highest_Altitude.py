class Solution(object):
    def largestAltitude(self, gain):
        diff_alti, max_alti = 0, 0
        for i in range(len(gain)):
            diff_alti += gain[i]
            if diff_alti > max_alti:
                max_alti = diff_alti

        return max_alti
    
gain = list(map(int, input().split()))
cls = Solution()
print(cls.largestAltitude(gain))
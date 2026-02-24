class Solution:
    def reverseString(self,s):
        left = 0
        n = len(s)
        right = n - 1

        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        return s

print(Solution().reverseString(["R","a","z","a"]))
class Solution:
    def leaders(self, arr):
        n = len(arr)
        result = []
        
        maxRight = arr[n-1]
        result.append(maxRight)
        
        for i in range(n-2, -1, -1):
            if arr[i] >= maxRight:
                maxRight = arr[i]
                result.append(maxRight)
        
        result.reverse()
        return result

print(Solution().leaders([16, 17, 4, 3, 5, 2]))
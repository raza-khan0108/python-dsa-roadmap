class Solution:
    def getMinMax(self, arr):
        n = len(arr)
        if (n == 0):
            return None, None
        
        min = arr[0]
        max = arr[0]
        
        for i in range(0,n):
            if(arr[i] < min):
                min = arr[i]
            
            if(arr[i] > max):
                max = arr[i]
        
        return min,max

print(Solution().getMinMax([1, 2, 3, 4, 5]))
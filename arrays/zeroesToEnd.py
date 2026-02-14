class Solution:
    def moveZeroesToEnd(self,arr):
        n = len(arr)
        if(n == 0):
            return None
        
        left = 0
        right = n-1 
        
        while left < right:
            if(arr[left] == 0):
                arr[left],arr[right] = arr[right], arr[left]
                right -= 1
            else:
                left += 1
        
        return arr

print(Solution().moveZeroesToEnd([0,10,5,0,20,40,0,60]))
class Solution:
    def moveZeroesToEnd(self,arr):
        n = len(arr)
        left = 0

        for right in range(n):
            if arr[right] != 0:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
        return arr

print(Solution().moveZeroesToEnd([0,10,5,0,20,40,0,60]))
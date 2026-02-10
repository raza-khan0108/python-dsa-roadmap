class Solution:
    def reverseArray(self,arr):
        left = 0
        right = len(arr)-1

        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
        return arr

array = [10,20,30,40,50,60]
print(Solution().reverseArray(array))
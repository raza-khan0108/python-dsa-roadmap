class Solution:
    def removeDuplicates(self,arr):
        n = len(arr)
        if (n == 0):
            return None
        
        index = 1
        for i in range(1,n):
            if arr[i] != arr[i-1]:
                arr[index] = arr[i]
                index += 1
        return arr[:index] 

print(Solution().removeDuplicates([1, 2, 2, 3, 4, 4, 5]))
class Solution:
    def isSorted(self,arr):
        n = len(arr) - 1
        for i in range(n):
            if(arr[i] >arr[i+1]):
                return False
        return True

array = [10,20,30,40,50,60]
print(Solution().isSorted(array))
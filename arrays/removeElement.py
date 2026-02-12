class Solution:
    def removeElement(self,arr,val):
        n =len(arr)
        if(n == 0):
            return None
        index = 0
        for i in range(n):
            if arr[i] != val:
                arr[index] = arr[i]
                index += 1
        return arr[:index]

print(Solution().removeElement([1, 2, 3, 4, 5], 5))
print(Solution().removeElement([1, 2, 3, 4, 5], 1))
print(Solution().removeElement([1, 2, 3, 4, 5], 3))
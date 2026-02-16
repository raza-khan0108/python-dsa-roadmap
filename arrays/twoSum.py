class Solution:
    def twoSum(self,arr,target):
        n = len(arr)
        if(n == 0):
            return None
        
        for i in range(n):
            for j in range(i+1,n):
                if(arr[i] + arr[j] == target):
                    return [i,j]
        
        return None

print(Solution().twoSum([2,7,11,15],9))
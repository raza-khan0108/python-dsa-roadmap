class Solution:
    def rotateArr(self,arr,k):
        n = len(arr)
        k = k % n
    
        temp = [0] * n
        for i in range(0,n):
            temp[(i+k)%n] = arr[i]            
        
        for i in range(0,n):
            arr[i] = temp[i]
            
        return arr
        
print(Solution().rotateArr([10,20,30,40,50,60],2))
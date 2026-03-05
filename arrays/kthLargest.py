import heapq
class Solution:
    def findKthLargest(self,nums,k):
        heap = []
        for num in nums:
            heapq.heappush(heap,num)

            if len(heap) > k:
                heapq.heappop(heap)
        
        return heap[0]

print(Solution().findKthLargest([3, 2, 1, 5, 6, 4], 3))
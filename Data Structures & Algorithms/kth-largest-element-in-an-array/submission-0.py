class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # sort and return kth index. O(nlogn) python sorting

        # heapify: O(N)
        # then pop max until kth pop. O(log(N-K)) per operation?
        # total: O(Nlog(N-K)), space: O(N) for heap

        # topK = []
        # for num in nums:
        # heapq.heappush(topK, num) O(log(k))
        # if len(topK) > k: heapq.heappop() Removes the min
        #  max: O(2log(k))?

        topK = []
        
        for num in nums:
            heapq.heappush(topK, num)
            if len(topK) > k:
                heapq.heappop(topK)
        
        # need to return the largest one but topK is unsorted. 
        # heappop() until last O(n)

        return min(topK)
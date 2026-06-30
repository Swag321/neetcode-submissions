class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        # heap [distance_a, distance_b, ...] O(k)
        # distance_a: [(x1,y1), (x2,y2)] O(k)

        # heappush is nlogn time?

        maxHeap = []
        
        for x,y in points:
            dist = x**2 + y**2
            entry = (-dist, x, y)
            heapq.heappush(maxHeap, entry)
            # push first, let heap sort, then remove the farthest if exceeds k
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        # ^ O(n)

        res = []
        while maxHeap:
            dist, x, y = heapq.heappop(maxHeap)
            res.append([x,y])
        
        return res



class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        minKD = [] # store here only the closest k distances
        
        for x,y in points:
            dist = -(x**2 + y**2)**(1/2) # make it negative to turn heap to max heap.
            entry = [dist, x, y]
            heapq.heappush(minKD, entry)
            if len(minKD) > k:
                heapq.heappop(minKD)
        
        # at this point minKD includes smallest k points

        result = []
        for dist,x,y in minKD:
            result.append([x,y])
        
        return result


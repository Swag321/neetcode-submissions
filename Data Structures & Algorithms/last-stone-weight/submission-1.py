class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        ns = [-stone for stone in stones]
        heapq.heapify(ns)

        while len(ns) > 1:
            m1, m2 = heapq.heappop(ns), heapq.heappop(ns)
            newWeight = m1 - m2
            if newWeight != 0:
                heapq.heappush(ns, newWeight)
            elif newWeight > 0:
                print("Error:", m1,m2,newWeight)
        ns.append(0)
        return -ns[0]
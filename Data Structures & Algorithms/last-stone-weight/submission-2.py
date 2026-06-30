class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # make it all negative
        s = [-stone for stone in stones]
        # turn to heap
        heapq.heapify(s)
        # until only 1 stone is left:
        while len(s) > 1:
            # keep smashing the biggest stones
            biggest, secondBiggest = heapq.heappop(s), heapq.heappop(s)
            newStone = biggest-secondBiggest
            if newStone != 0:
                heapq.heappush(s, newStone)
        
        return -s[0] if s else 0

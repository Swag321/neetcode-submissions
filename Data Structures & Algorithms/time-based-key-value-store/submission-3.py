class TimeMap:

    def __init__(self):
        #foo: [(bar,1), (bar,4)]
        self.keyToVT = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keyToVT[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyToVT[key]
        potentialWord = ""
        l,r = 0, len(values) -1
        #base cases:
        # if values[r][1] < timestamp:
        #     return values[r][0] # last word if timestamp is more
        # if timestamp < values[l][1]:
        #     return "" #nothing before this timestamp
        while l<=r:
            m = (l+r)//2
            mE = values[m][1]

            if timestamp >= mE:
                potentialWord = values[m][0]
                l = m+1
            elif timestamp < mE:
                r = m-1
        
        # #didn't find timestamp; return value to left of where it would've been
        # m = (l+r)//2
        # timestamp_prev = m - 1
        # if timestamp_prev < 0:
        #     return ""
        
        # return values[timestamp_prev][0]
        return values[r][0] if r>=0 else ""
        # return potentialWord


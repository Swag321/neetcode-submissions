class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        gts = defaultdict(set)
        cts = defaultdict(set)

        for y in range(len(board)):
            rowset = set()
            for x in range(len(board[y])):
                # going through the row
                val = board[y][x]
                if val == ".":
                    continue
                if val in rowset:
                    return False
                if val in cts[x]:
                    return False
                gridNum = x//3 + (y//3) * 3
                if val in gts[gridNum]:
                    return False
                rowset.add(val)
                cts[x].add(val)
                gts[gridNum].add(val)
        
        return True
                
            

            
            

            


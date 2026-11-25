class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        l,r = 0, len(s)-1

        while l<r:
            lc = s[l]
            rc = s[r]
            while not lc.isalnum():
                if l >= len(s)-1:
                    break
                l+= 1
                lc = s[l]
            while not rc.isalnum():
                if r <= 0:
                    break
                r-= 1
                rc = s[r]
            if not lc.isalnum() or not rc.isalnum():
                break
            if lc.lower() != rc.lower():
                return False
            
            l += 1
            r -= 1
            
        return True
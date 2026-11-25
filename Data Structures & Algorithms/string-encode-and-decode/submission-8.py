class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            length = len(word)
            encoded += str(length) + ":" + word
        
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        size = ""
        print(s)
        i = 0
        while i < len(s):
            char = s[i]
            print(char)
            if char == ":":
                jump = i + 1 + int(size) # jump to the size
                word = s[i+1:jump]
                # ^ substring from i+1 (skipping ":") to encoded length
                decoded.append(word)
                size = "" #reset size
                i = jump
            else:
                size += char
                #keep incr size until we reach ":". then grab substring of that size.
                i+=1
        return decoded

        


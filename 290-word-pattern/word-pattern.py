class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # Split the sentence into words
        words = s.split(" ")
        
        # Quick check: the number of words must match pattern length
        if len(words) != len(pattern):
            return False
        
        # Two mappings for bijective constraint
        MapWS = {}  # pattern char -> word
        MapSW = {}  # word -> pattern char
        
        for c, w in zip(pattern, words):
            # If c already mapped, it must map to the same word
            if c in MapWS and MapWS[c] != w:
                return False
            # If w already mapped, it must map to the same char
            if w in MapSW and MapSW[w] != c:
                return False
            
            # Record the mapping
            MapWS[c] = w
            MapSW[w] = c
        
        return True

    

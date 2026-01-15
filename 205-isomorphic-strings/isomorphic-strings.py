class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # If the lengths differ, they can't be isomorphic
        if len(s) != len(t):
            return False

        # Two dictionaries to store the character mappings
        mapST = {}
        mapTS = {}

        # Iterate through both strings at the same time
        for c1, c2 in zip(s, t):
            # If c1 was already mapped, check it maps to c2
            if c1 in mapST and mapST[c1] != c2:
                return False

            # If c2 was already mapped back, check it maps to c1
            if c2 in mapTS and mapTS[c2] != c1:
                return False

            # Record the mapping in both directions
            mapST[c1] = c2
            mapTS[c2] = c1

        # If no conflicts were found, they are isomorphic
        return True

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        FreqS,FreqT={},{}

        for ch in s:
            FreqS[ch]=FreqS.get(ch,0)+1
        for ch in t:
            FreqT[ch]=FreqT.get(ch,0)+1

        return FreqS==FreqT       
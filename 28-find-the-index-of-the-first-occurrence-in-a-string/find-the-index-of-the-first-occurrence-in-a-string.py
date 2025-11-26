class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle==" ":
            return 0
        idx=haystack.find(needle)
        return idx   
            
                
        
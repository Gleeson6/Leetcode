class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        table={}
        for ch in magazine:
            if ch in table:
                table[ch]+=1
            else:
                table[ch]=1
        for ch in ransomNote:
            if ch not in table or table[ch]==0:
                return False
            table[ch]-=1
        return True                     

        
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        while(len(s)==len(t)):
            return sorted(s) == sorted(t)   
        return False
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        while (len(s)==len(t)):
            counts = [0]*26
            for i in range (len(s)):
                counts[ord(s[i])-ord('a')]+= 1
                counts[ord(t[i])-ord('a')]-= 1
            for count in counts:
                if count!=0:
                    return False
            return True

        return False
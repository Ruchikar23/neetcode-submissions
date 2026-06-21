class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        else :
            freq = {}
            for i in s :
                freq[i] = freq.get(i,0) + 1
            for i in t :
                freq[i] = freq.get(i,0) - 1
            
            if all(value == 0 for value in freq.values()):
                return True 
            else :
                return False
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = s.split().pop()
        return len(a)
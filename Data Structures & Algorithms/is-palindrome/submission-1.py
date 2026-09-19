class Solution:
    def isPalindrome(self, s: str) -> bool:
        newText = "".join(c for c in s.lower() if c.isalnum())
        string2 = ""
        i = len(newText) - 1
        
        return newText == newText[::-1]
        
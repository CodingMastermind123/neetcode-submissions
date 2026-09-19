class Solution:
    def isPalindrome(self, s: str) -> bool:
        newText = "".join(c for c in s.lower() if c.isalnum())
        string2 = ""
        i = len(newText) - 1
        while i >= 0:
            string2 += newText[i]
            i -= 1

        if string2 == newText:
            return True
        
        return False
        
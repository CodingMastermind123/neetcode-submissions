class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            length = len(s)
        else:
            return False
        a = list(s)
        count = 0
        for i in t:
            if i in a:
                count += 1
                a.remove(i)
        if count == length:
            return True
        return False
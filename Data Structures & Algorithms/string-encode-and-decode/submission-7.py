class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return "empty"
        newStr = ""
        count = 0
        for i in strs:
            newStr += i
            if count < len(strs) - 1:
                newStr += "&&"
            count += 1
        return newStr

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return []
        newList = s.split("&&")
        return newList

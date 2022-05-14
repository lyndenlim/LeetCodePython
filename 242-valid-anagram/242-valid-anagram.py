class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sSplit = list(s)
        tSplit = list(t)
        sSplit.sort()
        tSplit.sort()
        return "".join(sSplit) == "".join(tSplit)
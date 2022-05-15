class Solution:
    def reverseVowels(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        sAsList = list(s)
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
        while left < right:
            if sAsList[left] not in vowels:
                left += 1
            else:
                if sAsList[right] not in vowels:
                    right -= 1
                else:
                    sAsList[left], sAsList[right] = sAsList[right], sAsList[left]
                    left += 1
                    right -= 1

        return "".join(sAsList)
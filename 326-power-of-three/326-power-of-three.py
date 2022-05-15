class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n % 3 == 0: 
            result = n
            counter = 0
            while result >= 3:
                result = result / 3
                counter += 1 
            return 3 ** counter == n
        elif n == 1: 
            return True
        return False
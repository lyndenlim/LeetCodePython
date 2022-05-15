class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n % 4 == 0: 
            result = n
            counter = 0
            while result >= 4:
                result = result / 4
                counter += 1 
            return 4 ** counter == n 
        elif n == 1: 
            return True
        return False
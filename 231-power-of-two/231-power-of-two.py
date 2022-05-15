class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        elif n % 2 == 0:
            counter = 0
            result = n
            while result >= 2:
                result = result / 2
                counter += 1
            return 2**counter == n
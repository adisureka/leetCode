class Solution:
    def isThree(self, n: int) -> bool:
        import math
        # common function to check for prime numbers
        def is_prime(p):
            if p <= 1:
                return False
            for i in range(2, int(p ** 0.5) + 1):
                if p % i == 0:
                    return False
            return True
        # Now check to see if the integer is a perfect square
        root = int(math.sqrt(n))
        if root * root != n:
            return False     
        # Check if square root of n is prime
        return is_prime(root)
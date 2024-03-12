import math

def isPowerOfTwo(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0: return False
    k = math.log(n, 2)
    if abs(k % 1) < 1e-10: return True
    return False

print(isPowerOfTwo(16))
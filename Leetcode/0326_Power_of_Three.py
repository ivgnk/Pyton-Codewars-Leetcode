import math

def isPowerOfThree(n):
    """
    :type n: int
    :rtype: bool
    """
    if n <= 0: return False
    k = math.log(n, 3)
    # print(f'{k=}')
    z = k % 1
    # print(f'{z=}')
    if abs(z) < 1e-10:
        return True
    else:
        if 1-z < 1e-10: return True
        else: return False

print(isPowerOfThree(243))
import math
def nearest_sq(n):
    res = math.sqrt(n)
    if res%1 <1e-9: return n;
    p1 = math.pow(int(res // 1),2)
    p2 = math.pow(int(res // 1)+1,2)
    if abs(n-p1)<abs(n-p2): return p1
    else: return p2

# Codewars best solution
#  def nearest_sq(n):
#     return round(n ** 0.5) ** 2
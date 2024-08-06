"""
06.08.2024. Topics: Array, Two Pointers
2511. Maximum Enemy Forts That Can Be Captured
https://leetcode.com/problems/maximum-enemy-forts-that-can-be-captured/

You are given a 0-indexed integer array forts of length n representing the positions of several forts.
forts[i] can be -1, 0, or 1 where:
-1 represents there is no fort at the ith position.
0 indicates there is an enemy fort at the ith position.
1 indicates the fort at the ith the position is under your command.
Now you have decided to move your army from one of your forts at position i to an empty position j such that:
0 <= i, j <= n - 1
The army travels over enemy forts only. Formally, for all k where min(i,j) < k < max(i,j), forts[k] == 0.
While moving the army, all the enemy forts that come in the way are captured.

Return the maximum number of enemy forts that can be captured.
In case it is impossible to move your army, or you do not have any fort under your command, return 0.

Example 1:
Input: forts = [1,0,0,-1,0,0,0,0,1]
Output: 4
Explanation:
- Moving the army from position 0 to position 3 captures 2 enemy forts, at 1 and 2.
- Moving the army from position 8 to position 3 captures 4 enemy forts.
Since 4 is the maximum number of enemy forts that can be captured, we return 4.

Example 2:
Input: forts = [0,0,1,-1]
Output: 0
Explanation: Since no enemy fort can be captured, 0 is returned.

Constraints:
1 <= forts.length <= 1000
-1 <= forts[i] <= 1
"""

# Runtime 21 ms Beats 64.00%
# Memory 11.75 MB Beats 24.00
# Runtime 17 ms Beats 96.00%
# Memory 11.82 MB Beats 12.00%

# Intuition
# Самое главное обойти проблему раздвоения рассмотрения между 1 и -1.
# То есть всегда рассматривать расстояние только от 1.
# Для этого нужен прямой и обратный проход от 1.

# Approach
# 1) Важно обойти крайние случаи: когда в массиве нет -1 или 0 или 1.
# 2) Важно обойти случай повторяющихся единиц, для этого случая счетчик нулей сбрасываем.
# 3) Реагировать на -1 и 0 надо только когда перед эти была 1, т.е. нужен  флаг этого числа

def captureForts(forts):
    """
    :type forts: List[int]
    :rtype: int
    """
    if 1 not in forts: return 0
    if 0 not in forts: return 0
    if -1 not in forts: return 0
    ll=len(forts)
    nn = 0; first=False
    # Stright
    for i in range(ll):
        if forts[i]==1:
            first=True
            count = 0
        elif forts[i]==0 and first:
            count+=1
        elif forts[i]==-1 and first:
            nn=max(nn,count)
            first = False
            count = 0

    first = False; count = 0
    # Reverse
    for i in range(ll-1,-1,-1):
        if forts[i]==1:
            first=True
            count = 0
        elif forts[i]==0 and first:
            count+=1
        elif forts[i]==-1 and first:
            nn=max(nn,count)
            first = False
            count = 0

    return nn


# print(captureForts([1,0,0,-1,0,0,0,0,1])) # 4
# print(captureForts([0,0,1,-1])) # 0
# print(captureForts([1,0,0,-1,0,0,-1,0,0,1])) # 2
# print(captureForts([1,-1,-1,1,1])) # 0
# print(captureForts([-1,0,-1,0,1,1,1,-1,-1,-1])) #
# print(captureForts([-1,0,-1,0,1,1,1,-1,-1,-1]))
print(captureForts([-1,-1,0,1,0,0,1,-1,1,0]))   #1






# Runtime 385 ms Beats 8.00%
# Memory 11.67 MB Beats 72.00%
def captureForts2(forts):
    """
    :type forts: List[int]
    :rtype: int
    """
    ll=len(forts)
    np1=[i for i in range(ll) if forts[i]==1]
    nm1=[i for i in range(ll) if forts[i]==-1]
    if ll==len(nm1)+len(np1): return 0
    # reverse=False
    nn=0
    for p1 in np1:
        for m1 in nm1:
            if m1>p1 and forts[p1:m1+1].count(0)==m1-p1-1:
                nn=max(nn,m1-p1-1)
                break
    # reverse=True
    np1=list(reversed(np1))
    nm1=list(reversed(nm1))
    for p1 in np1: # +
        for m1 in nm1:
            if p1>m1 and forts[m1:p1+1].count(0)==p1-m1-1:
                nn=max(nn,p1-m1-1)
                break
    return nn



"""
Done 06.11.2024. Topics: Sorting
3011. Find if Array Can Be Sorted
https://leetcode.com/problems/find-if-array-can-be-sorted/

You are given a 0-indexed array of positive integers nums.
In one operation, you can swap any two adjacent elements if they have the same number of set bits.
You are allowed to do this operation any number of times (including zero).
Return true if you can sort the array, else return false.

Example 1:
Input: nums = [8,4,2,30,15]
Output: true
Explanation: Let's look at the binary representation of every element. The numbers 2, 4, and 8 have one set bit each with binary representation "10", "100", and "1000" respectively. The numbers 15 and 30 have four set bits each with binary representation "1111" and "11110".
We can sort the array using 4 operations:
- Swap nums[0] with nums[1]. This operation is valid because 8 and 4 have one set bit each. The array becomes [4,8,2,30,15].
- Swap nums[1] with nums[2]. This operation is valid because 8 and 2 have one set bit each. The array becomes [4,2,8,30,15].
- Swap nums[0] with nums[1]. This operation is valid because 4 and 2 have one set bit each. The array becomes [2,4,8,30,15].
- Swap nums[3] with nums[4]. This operation is valid because 30 and 15 have four set bits each. The array becomes [2,4,8,15,30].
The array has become sorted, hence we return true.
Note that there may be other sequences of operations which also sort the array.

Example 2:
Input: nums = [1,2,3,4,5]
Output: true
Explanation: The array is already sorted, hence we return true.

Example 3:
Input: nums = [3,16,8,4,2]
Output: false
Explanation: It can be shown that it is not possible to sort the input array using any number of operations.

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 2**8

Hint 1
Split the array into segments. Each segment contains consecutive elements with the same number of set bits.
Hint 2
From left to right, the previous segment’s largest element should be smaller than the current segment’s smallest element.

My solution https://leetcode.com/problems/find-if-array-can-be-sorted/solutions/6015277/fast-7-ms-but-long-python-solution-for-problem-3011/
✏️ Fast (7 ms), but long Python solution for Problem 3011

Intuition
Everything you need is in the description, examples and hints,
but all this should be taken literally and not speculated.
Seemingly simple solutions will lead to errors in the latest tests.

Do it in order:
- Index each number by the number of units in binary representation
- Group by the number of units observing the order,
i.e. not combining broken groups with an equal number of units
- Find the minimum and maximum for each group
- For each group, apply:
From left to right, the previous segment's largest element should be smaller
than the current segment's smallest element.
"""

# Runtime 7 ms Beats 78.18%
# Memory 16.76 MB Beats 23.35%
# Time Complexity O(NLogN)
# Space Complexity O(N)
def canSortArray(nums):
    if nums == sorted(nums): return True
    ll = len(nums)
    ddl=list()
    # --1 Indexes
    for i in range(ll):
        nn = bin(nums[i])[2:].count('1')
        ddl.append((nn,nums[i]))
    ddl2=[[ ddl[0][0], [ddl[0][1]]]]
    n=0
    print(f'{ddl=}')
    # --2 Groyp by Indexes
    for i in range(1,ll):
        if ddl[i][0]==ddl[i-1][0]:
            ddl2[n][1].append(ddl[i][1])
        else:
            ddl2.append([ddl[i][0],[ddl[i][1]]])
            n+=1
    print(f'{ddl2=}')
    # --3 Test for sort
    ma_x=max(ddl2[0][1])
    # print(f'{mi_x=} {ma_x=}')
    for i in range(1,len(ddl2)):
        if ddl2[i][0]!=ddl2[i-1][0]:
            mi_xn = min(ddl2[i][1])
            ma_xn = max(ddl2[i][1])
            print(f'{i=} {mi_xn=} {ma_xn=}')
            if mi_xn>ma_x:
                ma_x = ma_xn
            else: return False
    return True

# print(canSortArray([8,4,2,30,15])) # True
# print(canSortArray([1,2,3,4,5]))
# print(canSortArray([3,16,8,4,2]))
# print(canSortArray([24,12]))
# print(canSortArray([107,76,52])) # False
print(canSortArray([174, 175, 234, 188]))


ksrt=lambda x: (x[0].count('1'), x[1])
# Wrong Answer- 720 / 999 testcases passed. Not pass Case 3
def canSortArray2(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums == sorted(nums): return True
    ll = len(nums)
    lst = [(bin(nums[i])[2:], nums[i]) for i in range(ll)]
    lst2 = sorted(lst, key=ksrt)
    for i in range(1, ll):
        if lst2[i] < lst2[i - 1]: return False
    return True

# Wrong Answer - 967 / 999 testcases passed
ksrt2=lambda x: (x[0], x[1])
def canSortArray3(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums == sorted(nums): return True
    ll=len(nums)
    if ll==2:
        if bin(nums[0])[2:].count('1') != bin(nums[1])[2:].count('1') : return False
    lst=[]
    for i in range(ll):
        s=bin(nums[i])[2:]
        lst.append((s.count('1'), nums[i], s))
    lst2=sorted(lst, key=ksrt2)
    print(lst2)
    # print('----------')
    for i in range(1,ll):
        if lst2[i-1][1]>lst2[i][1]:
            # print('---',lst2[i-1][1],lst2[i][1],lst2[i-1][1]>lst2[i][1])
            return False
    return True

# Wrong Answer - 970 / 999 testcases passed
ksrt3=lambda x: (x[0], x[1])
import itertools
def canSortArray4(nums):
    if nums == sorted(nums): return True
    ll = len(nums)
    if ll==2:
        if bin(nums[0])[2:].count('1') != bin(nums[1])[2:].count('1') : return False
    elif ll==3:
        if bin(nums[0])[2:].count('1') != bin(nums[1])[2:].count('1') != bin(nums[2])[2:].count('1'): return False

    lst=[]
    for i in range(ll):
        s=bin(nums[i])[2:]
        lst.append((s.count('1'), nums[i], s))
    print(f'{lst=}')
    lst2=sorted(lst)
    # print(f'{lst2=}')
    for i in range(1,ll):
        if lst2[i-1][1]>lst2[i][1]:
            # print('---',lst2[i-1][1],lst2[i][1],lst2[i-1][1]>lst2[i][1])
            return False
    return True

    # for i, group in itertools.groupby(lst, ksrt2):
    #     print(i)
        # for fruit in group:
        #     print(fruit['name'])

ksrt4=lambda x: x[1]
def canSortArray5(nums):
    ll = len(nums)
    lst=[]
    for i in range(ll):
        s=bin(nums[i])[2:]
        lst.append((s.count('1'), nums[i], s))
    print(f'{lst=}')
    lst2 = sorted(lst)
    print(f'{lst2=}')
    for i, group in itertools.groupby(lst2, ksrt4):
        print(f'{i}=')
        for dat in group:
            print(f'{dat=}')

# Wrong Answer - 998 / 999 testcases passed
def canSortArray6(nums):
    if nums == sorted(nums): return True
    ll = len(nums)
    dd=dict()
    lst=list()
    for i in range(ll):
        nn = bin(nums[i])[2:].count('1')
        if nn in dd:
            dd[nn].append(nums[i])
        else:
            dd[nn] = [nums[i]]
        lst.append((nn,nums[i]))
    print(f'{dd=}')
    print(f'{lst=}')
    dd2=dict()
    for k,v in dd.items():
        dd2[k]=(v, min(v), max(v))
    print(f'{dd2=}')
    mi_x=dd2[lst[0][0]][1]
    ma_x=dd2[lst[0][0]][2]
    print(f'{mi_x=} {ma_x=}')
    for i in range(1,ll):
        if lst[i][0]!=lst[i-1][0]:
            mi_xn = dd2[lst[i][0]][1]
            ma_xn = dd2[lst[i][0]][2]
            print(f'{i=} {mi_xn=} {ma_xn=}')
            if mi_xn>ma_x:
                mi_x = mi_xn;   ma_x = ma_xn
            else: return False
    return True


"""
Done 06.08.2024. Topics: Array, Sliding Window
1004. Max Consecutive Ones III
https://leetcode.com/problems/max-consecutive-ones-iii/

Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

Example 1:
Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Example 2:
Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

Constraints:
1 <= nums.length <= 10**5
nums[i] is either 0 or 1.
0 <= k <= nums.length

Hint 1
One thing's for sure, we will only flip a zero if it extends an existing window of 1s.
Otherwise, there's no point in doing it, right? Think Sliding Window!
--
Одно можно сказать наверняка: мы перевернем ноль только в том случае, если он расширит существующее окно в 1с.
Иначе нет смысла это делать, верно? Подумайте о раздвижном окне!

Hint 2
Since we know this problem can be solved using the sliding window construct,
we might as well focus in that direction for hints. Basically,
in a given window, we can never have > K zeros, right?
--
Поскольку мы знаем, что эту проблему можно решить с помощью конструкции скользящего окна,
мы могли бы сосредоточиться на этом направлении и получить подсказки.
По сути, в данном окне мы никогда не можем иметь > K нулей, верно?


Hint 3
We don't have a fixed size window in this case.
The window size can grow and shrink depending upon the number of zeros we have
(we don't actually have to flip the zeros here!).
--
В этом случае у нас нет окна фиксированного размера. Размер окна может увеличиваться и уменьшаться в зависимости от
количества имеющихся у нас нулей (здесь нам не нужно переворачивать нули!).

Hint 4
The way to shrink or expand a window would be based on the number
of zeros that can still be flipped and so on.
--
Способ уменьшения или расширения окна будет зависеть от количества нулей,
которые еще можно перевернуть, и так далее.
"""
from icecream import ic

# Runtime 454 ms Beats 31.19% Analyze Complexity
# Memory 12.02 MB Beats 75.66%
def longestOnes(nums, k):
    i = 0
    count = 0
    j = 0
    m_size = 0
    while j < len(nums):
        if nums[j] == 0:
            count += 1
        while count > k:
            if nums[i] == 0:
                count -= 1
            i += 1
        j += 1
        m_size = max(m_size, j - i)
    return m_size

#                      0  1  2  3  4  5  6  7  8  9  10
ic(longestOnes(nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k = 2))  # 6
ic(longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)) # 10

# Runtime 427 ms Beats 83.17%
# Memory 12.56 MB Beats 11.10%
def longestOnes0(nums, k):
    l = r = 0
    for r in range(len(nums)):
        if nums[r] == 0:
            k -= 1
        if k < 0:
            if nums[l] == 0:
                k += 1
            l += 1
        ic(r,'  ', l,r,k)
    return r - l + 1



# Runtime 7098 ms Beats 5.03%
# Memory 12.83 MB Beats 11.1
def longestOnes1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll = len(nums); n0 = nums.count(0)
    if n0 == ll:
        if n0 <= k: return ll
        else: return 0
    elif n0 + 1 == ll:
        return min(ll, k + 1)

    nn = 0
    for i in range(ll):
        if nums[i] == 1:
            nn += 1; arr = [1]; res = [1]
            break
    j = i + 1
    while j < ll:
        arr.append(nums[j])
        if arr.count(0) <= k:
            nn += 1
            res.append(len(arr))
        else:
            arr.pop(0)
            nn -= 1
        j += 1
    res.append(nn)

    return max(res)




def longestOnes2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    ll=len(nums); nn=0
    # Find first left edge
    for i in range(ll):
        if nums[i]==1:
            nn += 1; break

    res=[1]
    j=i+1; k1=0
    ic(i,j)
    while j<ll:
        # ic('bef',i,j,nn,k1,nums[j])
        ic('bef', j, nums[i:j+1],k1)
        if nums[j]==1:
            nn += 1
            j=j+1
            if k1>0: k1 -=1
            res.append(nn)
        elif k1<k: # nums[j]==0
            k1 +=1
            nn += 1
            j=j+1
            res.append(nn)
        elif k1==k:  #  nums[j]==0
            res.append(nn)
            k1 +=1
            i = i+1
            j += 1
            nn -= 1
        else: # k1>k nums[j]==0
            i = i+1
            j += 1
            nn=0
        if j<ll:
            ic('aft',i,j,nn,k1,res)
            ic(' ')
    res.append(nn)

    return max(res)


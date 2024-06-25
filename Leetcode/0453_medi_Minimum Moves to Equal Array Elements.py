"""
Done 25.06.2024. Topics: Array, Math
453. Minimum Moves to Equal Array Elements
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

Given an integer array nums of size n,
return the minimum number of moves required to make all array elements equal.
In one move, you can increment n - 1 elements of the array by 1.

Example 1:
Input: nums = [1,2,3]
Output: 3
Explanation: Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]

Example 2:
Input: nums = [1,1,1]
Output: 0

as hint https://leetcode.com/problems/minimum-moves-to-equal-array-elements/description/comments/1565359
Известно: порядковые номера, начальная сумма s0, длина n, наименьшее число — m.
Предположим, мы продвинулись на k шагов Каждый раз, когда вы перемещаетесь на один шаг,
n-1 чисел будет +1, тогда итоговая сумма s = s0 +(n-1) x k.
Среднее значение з/п Минимальное число — +1 для каждого хода, поэтому имеем:
k =s/n -m. То есть: (s0 +(n-1) x k)/n -m =k
Найти: k = s0 - m x n
"""

# Runtime 183 ms Beats 63.64%
# Memory 12.91 MB Beats 13.64%
# Runtime 177 ms Beats 86.36%
# Memory 12.72 MB Beats 27.27%

def minMoves(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    s0=sum(nums)
    m=min(nums)
    n=len(nums)
    return s0-m*n

print(minMoves([1,2,3]))
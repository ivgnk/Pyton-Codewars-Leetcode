"""
Done 09.03.2025
3477. Fruits Into Baskets II
https://leetcode.com/problems/fruits-into-baskets-ii/description/

You are given two arrays of integers, fruits and baskets, each of length n,
where fruits[i] represents the quantity of the ith type of fruit,
and baskets[j] represents the capacity of the jth basket.

From left to right, place the fruits according to these rules:

Each fruit type must be placed in the leftmost available basket
with a capacity greater than or equal to the quantity of that fruit type.
Each basket can hold only one type of fruit.
If a fruit type cannot be placed in any basket, it remains unplaced.
Return the number of fruit types that remain unplaced after all possible
allocations are made.

Example 1:
Input: fruits = [4,2,5], baskets = [3,5,4]
Output: 1
Explanation:
fruits[0] = 4 is placed in baskets[1] = 5.
fruits[1] = 2 is placed in baskets[0] = 3.
fruits[2] = 5 cannot be placed in baskets[2] = 4.
Since one fruit type remains unplaced, we return 1.

Example 2:
Input: fruits = [3,6,1], baskets = [6,4,7]
Output: 0
Explanation:
fruits[0] = 3 is placed in baskets[0] = 6.
fruits[1] = 6 cannot be placed in baskets[1] = 4 (insufficient capacity) but can be placed in the next available basket, baskets[2] = 7.
fruits[2] = 1 is placed in baskets[1] = 4.
Since all fruits are successfully placed, we return 0.

Constraints:
n == fruits.length == baskets.length
1 <= n <= 100
1 <= fruits[i], baskets[i] <= 1000

Hint 1
Simulate the operations for each fruit as described

My solution
✏️ Easy Python solution for Problem 3477
https://leetcode.com/problems/fruits-into-baskets-ii/solutions/6516994/easy-python-solution-for-problem-3477-by-jgsf/

Intuition
The restrictions are light, so we use nested loops.:
- external fruit cycle
- an internal cycle through the baskets
Important: for basket numbers, use a dictionary instead of a list.
"""

# Runtime 31 ms Beats 100.00%
# Memory 12.28 MB Beats 100.00%
# Time Complexity O(N∗M)
# Space Complexity O(M)
def numOfUnplacedFruits(fruits, baskets):
    """
    :type fruits: List[int]
    :type baskets: List[int]
    :rtype: int
    """
    lf=len(fruits)
    bs={i:baskets[i] for i in range(len(baskets))}
    rem_=lf
    for i in range(lf):
        for kb,vb in bs.items():
            if vb>=fruits[i]:
                del bs[kb]
                rem_-=1
                break
    return rem_

print(numOfUnplacedFruits(fruits = [4,2,5], baskets = [3,5,4]))
print(numOfUnplacedFruits(fruits = [3,6,1], baskets = [6,4,7]))

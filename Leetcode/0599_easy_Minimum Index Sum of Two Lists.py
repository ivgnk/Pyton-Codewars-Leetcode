"""
Done 17.09.2024. Topics: Hash Table, String
599. Minimum Index Sum of Two Lists
https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

Given two arrays of strings list1 and list2, find the common strings with the least index sum.
A common string is a string that appeared in both list1 and list2.

A common string with the least index sum is a common string such that if it appeared at
list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.

Return all the common strings with the least index sum. Return the answer in any order.

Example 1:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only common string is "Shogun".

Example 2:
Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The common string with the least index sum is "Shogun" with index sum = (0 + 1) = 1.

Example 3:
Input: list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]
Output: ["sad","happy"]
Explanation: There are three common strings:
"happy" with index sum = (0 + 1) = 1.
"sad" with index sum = (1 + 0) = 1.
"good" with index sum = (2 + 2) = 4.
The strings with the least index sum are "sad" and "happy".

Constraints:

1 <= list1.length, list2.length <= 1000
1 <= list1[i].length, list2[i].length <= 30
list1[i] and list2[i] consist of spaces ' ' and English letters.
All the strings of list1 are unique.
All the strings of list2 are unique.
There is at least a common string between list1 and list2.

Solution
✏️ Compact (4 lines) Python solution
Intuition
- Find common strings
- Create dictionary with index sum
- Find min in dictionary
- Create result with using list comprehension
https://leetcode.com/problems/minimum-index-sum-of-two-lists/post-solution/?submissionId=1393053810
"""

# Runtime 200 ms Beats 49.46% Analyze Complexity
# Memory 12.28 MB Beats 14.75%
def findRestaurant2(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    d1 = {list1[i]:i for i in range(len(list1))}
    d2 = {list2[i]:i for i in range(len(list2))}
    l3 = list(set(list1)&set(list2))
    d3 = {}
    mmin=30000
    for k in l3:
        d3[k]=d1[k]+d2[k]
        mmin=min(mmin,d3[k])
    return [k for k,v in d3.items() if v==mmin]

# Runtime 238 ms Beats 42.30%
# Memory 12.06 MB Beats 77.66%
# Runtime 236 ms Beats 42.52%
# Memory 12.07 MB Beats 77.66%
def findRestaurant1(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    # d1 = {list1[i]:i for i in range(len(list1))}
    # d2 = {list2[i]:i for i in range(len(list2))}
    l3 = list(set(list1)&set(list2))
    d3 = {}
    mmin=30000
    for k in l3:
        d3[k]=list1.index(k)+list2.index(k)
        mmin=min(mmin,d3[k])
    return [k for k,v in d3.items() if v==mmin]


# Runtime 235 ms Beats 42.73%
# Memory 11.99 MB Beats 94.58%
def findRestaurant(list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """
    l3 = list(set(list1)&set(list2))
    d3 = {k:list1.index(k)+list2.index(k) for k in l3}
    mmin=min(d3.values())
    return [k for k,v in d3.items() if v==mmin]


print(findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"],
                     list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]))

# print(findRestaurant(list1 = ["happy","sad","good"], list2 = ["sad","happy","good"]))


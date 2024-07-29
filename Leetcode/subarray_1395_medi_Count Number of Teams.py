"""
29.07.2024. Topics: Array
1395. Count Number of Teams
https://leetcode.com/problems/count-number-of-teams

There are n soldiers standing in a line. Each soldier is assigned a unique rating value.
You have to form a team of 3 soldiers amongst them under the following rules:

Choose 3 soldiers with index (i, j, k) with rating (rating[i], rating[j], rating[k]).
A team is valid if: (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k])
where (0 <= i < j < k < n).
Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

Example 1:
Input: rating = [2,5,3,4,1]
Output: 3
Explanation: We can form three teams given the conditions. (2,3,4), (5,4,1), (5,3,1).

Example 2:
Input: rating = [2,1,3]
Output: 0
Explanation: We can't form any team given the conditions.

Example 3:
Input: rating = [1,2,3,4]
Output: 4


Constraints:
n == rating.length
3 <= n <= 1000
1 <= rating[i] <= 10**5
All the integers in rating are unique.

Hint 1
BruteForce, check all possibilities - This hint work in C++ & Rust, but not work in Python

True tip
https://leetcode.com/problems/count-number-of-teams/description/comments/2545404
No DFS, No Recursion, No Memorization
For each element in [1:n-1] in the array,
checks for smaller elements on the left and larger elements on the right and then multiply their counts and add it to res.
checks for larger elements on the left and smaller elements on the right and then multiply their counts and add it to res.
"""

# Time Limit Exceeded - 60 / 72 testcases passed
def numTeams2(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    ll=len(rating); n=0
    for i in range(ll):
        for j in range(i+1,ll):
            for k in range(j + 1, ll):
                if (rating[i] < rating[j] < rating[k]) or (rating[i] > rating[j] > rating[k]):
                    n=n+1
    return n

# Time Limit Exceeded - 60 / 72 testcases passed
def numTeams3(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    ll=len(rating); n=0
    for i in range(ll):
        for j in range(i+1,ll):
            for k in range(j + 1, ll):
                if rating[i] < rating[j]:
                    if rating[j]< rating[k]:
                        n=n+1
                if rating[i] > rating[j]:
                    if rating[j] > rating[k]:
                        n = n + 1
    return n

# Time Limit Exceeded - 63 / 72 testcases passed
def numTeams4(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    ll=len(rating); n=0
    print(ll)
    for i in range(ll):
        for j in range(i+1,ll):
            if rating[i] < rating[j]:
                for k in range(j + 1, ll):
                    if rating[j]< rating[k]:
                        n=n+1
            elif rating[i] > rating[j]:
                for k in range(j + 1, ll):
                    if rating[j] > rating[k]:
                        n = n + 1
    return n

# Time Limit Exceeded - 62 / 72 testcases passed
def numTeams5(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    ll=len(rating); n=0
    print(ll)
    for i in range(ll):
        for j in range(i+1,ll):
            if rating[i] < rating[j]:
                for k in range(j + 1, ll):
                    n=n+(rating[j]< rating[k])
            elif rating[i] > rating[j]:
                for k in range(j + 1, ll):
                    n = n +(rating[j] > rating[k])
    return n

# Runtime 1022 ms Beats 16.67%
# Memory 11.95 MB Beats 13.33%
def numTeams6(rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    ll=len(rating); n=0
    print(ll)
    for i in range(1,ll-1):
        left=rating[:i]
        right=rating[i+1:]
        mil=min(left); mar=max(right)
        mal=max(left); mir=min(right)
        n=n+mil*mar+mal*mir
    return n

# Runtime 716 ms Beats 73.33%
# Memory 11.73 MB Beats 66.67%
def numTeams(self, rating):
    """
    :type rating: List[int]
    :rtype: int
    """
    n = len(rating)
    count = 0

    for j in range(n):
        leftLess = leftGreater = rightLess = rightGreater = 0

        for i in range(j):
            if rating[i] < rating[j]:
                leftLess += 1
            elif rating[i] > rating[j]:
                leftGreater += 1

        for k in range(j + 1, n):
            if rating[k] < rating[j]:
                rightLess += 1
            elif rating[k] > rating[j]:
                rightGreater += 1

        count += leftLess * rightGreater + leftGreater * rightLess

    return count

print(numTeams(rating = [2,5,3,4,1])) # 3
print(numTeams(rating = [2,1,3])) # 0
print(numTeams(rating = [1,2,3,4])) # 4

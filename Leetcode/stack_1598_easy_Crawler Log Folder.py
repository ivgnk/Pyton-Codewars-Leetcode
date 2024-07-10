"""
Done 10.07.2024. Topics: Array, String

1598. Crawler Log Folder
https://leetcode.com/problems/crawler-log-folder/description

The Leetcode file system keeps a log each time some user performs a change folder operation.
The operations are described below:
"../" : Move to the parent folder of the current folder.
(If you are already in the main folder, remain in the same folder).
"./" : Remain in the same folder.
"x/" : Move to the child folder named x (This folder is guaranteed to always exist).
You are given a list of strings logs where logs[i] is the operation performed by the user at the ith step.

The file system starts in the main folder, then the operations in logs are performed.

Return the minimum number of operations needed to go back to the main folder
after the change folder operations.

Example 1:
Input: logs = ["d1/","d2/","../","d21/","./"]
Output: 2
Explanation: Use this change folder operation "../" 2 times and go back to the main folder.

Example 2:
Input: logs = ["d1/","d2/","./","d3/","../","d31/"]
Output: 3

Example 3:
Input: logs = ["d1/","../","../","../"]
Output: 0

Hint 1
Simulate the process but don’t move the pointer beyond the main folder.
"""

# Runtime 28 ms Beats 40.12%
# Time Complexity O(N)
# Memory 11.91 MB Beats 23.2
# Space Complexity O(1)

# Runtime 19 ms Beats 93.02%
# Memory 11.97 MB Beats 23.26%
def minOperations(logs):
    """
    :type logs: List[str]
    :rtype: int
    """
    n=0
    for s in logs:
        if s=="./":
            continue
        elif s=="../":
            if n!=0: n=n-1
        else:
            n = n + 1
    return n
print(minOperations(["d1/","d2/","../","d21/","./"]))
print(minOperations(["d1/","d2/","./","d3/","../","d31/"]))
print(minOperations(["d1/","../","../","../"]))


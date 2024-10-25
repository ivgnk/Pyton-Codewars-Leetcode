"""
Done 25.10.2024. Topics: Array, String
1233. Remove Sub-Folders from the Filesystem
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/description/

Given a list of folders folder, return the folders after removing all sub-folders in those folders.
You may return the answer in any order.

If a folder[i] is located within another folder[j], it is called a sub-folder of it.
A sub-folder of folder[j] must start with folder[j], followed by a "/".
For example, "/a/b" is a sub-folder of "/a", but "/b" is not a sub-folder of "/a/b/c".

The format of a path is one or more concatenated strings of the form:
'/' followed by one or more lowercase English letters.

For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string and "/" are not.

Example 1:
Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
Output: ["/a","/c/d","/c/f"]
Explanation: Folders "/a/b" is a subfolder of "/a" and "/c/d/e" is inside of folder "/c/d" in our filesystem.

Example 2:
Input: folder = ["/a","/a/b/c","/a/b/d"]
Output: ["/a"]
Explanation: Folders "/a/b/c" and "/a/b/d" will be removed because they are subfolders of "/a".

Example 3:
Input: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
Output: ["/a/b/c","/a/b/ca","/a/b/d"]

Constraints:
1 <= folder.length <= 4 * 104
2 <= folder[i].length <= 100
folder[i] contains only lowercase letters and '/'.
folder[i] always starts with the character '/'.
Each folder name is unique.

Hint 1
Sort the folders lexicographically.
Hint 2
Insert the current element in an array and then loop until we get rid of all of their subfolders,
repeat this until no element is left.

My solution
✏️ Fast and easy Python solution for Problem 1233
https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/solutions/5966451/fast-and-easy-python-solution-for-problem-1233/

Intuition
Use Hints.
Use function startswith.
Remember to call the replace function correctly in our case

Easiest problem for Python.
Often the Topics are incorrect in Leetcode.
Тrue topics are "Array, String".
Topics "Depth-First Search, Trie" are confusing
"""

# Runtime 27 ms Beats 92.41%
# Memory 29.60 MB Beats 93.10%
# Time Complexity O(NLogN)
# Space Complexity O(N)
def removeSubfolders(folder):
    """
    :type folder: List[str]
    :rtype: List[str]
    """
    f=sorted(folder)
    res=[f[0]]
    for i in range(1,len(f)):
        if not f[i].startswith(res[-1]):
            res.append(f[i])
        else:
            rest=f[i].replace(res[-1],'',1)
            if rest[0] != '/': res.append(f[i])
    return res

# print(removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"]))
# print(removeSubfolders(["/a","/a/b/c","/a/b/d"]))
print(removeSubfolders(["/a/b/c","/a/b/ca","/a/b/d"]))

prf='/a'
s='/a/aaaaa'
print(s.replace(prf,'',1))
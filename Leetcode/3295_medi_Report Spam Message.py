"""
Done 22.09.2024. Topics: Array, String
3295. Report Spam Message
https://leetcode.com/problems/report-spam-message/description/
You are given an array of strings message and an array of strings bannedWords.
An array of words is considered spam if there are at least two words
in it that exactly match any word in bannedWords.
Return true if the array message is spam, and false otherwise.

Example 1:
Input: message = ["hello","world","leetcode"], bannedWords = ["world","hello"]
Output: true
Explanation:
The words "hello" and "world" from the message array both appear in the bannedWords array.

Example 2:
Input: message = ["hello","programming","fun"], bannedWords = ["world","programming","leetcode"]
Output: false
Explanation:
Only one word from the message array ("programming") appears in the bannedWords array.

Constraints:
1 <= message.length, bannedWords.length <= 105
1 <= message[i].length, bannedWords[i].length <= 15
message[i] and bannedWords[i] consist only of lowercase English letters.

Hint 1
Use hash set

✏️ Not obvious Python solution because  tricky problem description
Intuition
A tricky description of the task: it does not say what the array of banned words is.
The TLE error occurs because banned words are repeated!!!!

Approach
When you understand tricky description, then use a set

Done 22.09.2024.
Runtime 2462 ms Beats 100.00%
Memory 55.99 MB Beats 100.00%
"""


# Time Limit Exceeded - 522 / 526 testcases passed
def reportSpam2(message, bannedWords):
    """
    :type message: List[str]
    :type bannedWords: List[str]
    :rtype: bool
    """
    n=0
    for s in message:
       if s in bannedWords:
           n+=1
           if n==2: return True
    return False

# Time Limit Exceeded - 522 / 526 testcases passed
def reportSpam3(message, bannedWords):
    dd=dict(); n=0
    for s in message:
        if s in dd:
            dd[s]+=1
        else:
            dd[s]=1
        if s in bannedWords:
            n+=1
            if n==2: return True
    return False

# Wrong Answer - 514 / 526 testcases passed
# message = ["l","i","l","i","l"]
# bannedWords = ["d","a","i","v","a"]
def reportSpam4(message, bannedWords):
    m=set(message)
    b=set(bannedWords)
    return len(m & b)>=2

def reportSpam5(message, bannedWords):
    dd = dict(); n = 0
    for s in message:
        if s in dd:
            dd[s] += 1
        else:
            dd[s] = 1

    for k, v in dd.items():
        if k in bannedWords:
            n += v
            if n >= 2: return True
    return False

# Runtime 2446 ms Beats 100.00%
# Memory 55.70 MB Beats 100.00%
# Runtime 2462 ms Beats 100.00%
# Memory 55.99 MB Beats 100.00%
from collections import Counter
def reportSpam(message, bannedWords):
    b = set(bannedWords)
    n = 0
    for word in message:
        if word in b:
            n += 1
    return n >= 2
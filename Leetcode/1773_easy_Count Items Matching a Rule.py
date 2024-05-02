"""
Done 02.05.2024
1773. Count Items Matching a Rule
https://leetcode.com/problems/count-items-matching-a-rule/description/

You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color,
and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.

The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule.

Example 1:
Input: items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]],
ruleKey = "color", ruleValue = "silver"
Output: 1
Explanation: There is only one item matching the given rule, which is ["computer","silver","lenovo"].

Example 2:
Input: items = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
ruleKey = "type", ruleValue = "phone"
Output: 2
Explanation: There are only two items matching the given rule, which are ["phone","blue","pixel"] and
["phone","gold","iphone"]. Note that the item ["computer","silver","phone"] does not match.
"""

# Runtime 173 ms Beats 90.94% of users with Python
# Memory 19.18 MB Beats 84.90% of users with Python

def countMatches(items, ruleKey, ruleValue):
    """
    :type items: List[List[str]]
    :type ruleKey: str
    :type ruleValue: str
    :rtype: int
    """
    return sum(1 for i in items if (ruleKey=="type" and  ruleValue==i[0]) or
               (ruleKey=="color" and  ruleValue==i[1]) or
               (ruleKey == "name" and ruleValue == i[2]))

# print(countMatches())
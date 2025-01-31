"""
Done 31.01.2025.
3436. Find Valid Emails
SQL Schema
Pandas Schema
Table: Users
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
(user_id) is the unique key for this table.
Each row contains a user's unique ID and email address.
Write a solution to find all the valid email addresses. A valid email address meets the following criteria:

It contains exactly one @ symbol.
It ends with .com.
The part before the @ symbol contains only alphanumeric characters and underscores.
The part after the @ symbol and before .com contains a domain name that contains only letters.
Return the result table ordered by user_id in ascending order.

Example:
Input:
Users table:
+---------+---------------------+
| user_id | email               |
+---------+---------------------+
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
+---------+---------------------+

Output:
+---------+-------------------+
| user_id | email             |
+---------+-------------------+
| 1       | alice@example.com |
| 4       | david@domain.com  |
+---------+-------------------+

Explanation:
alice@example.com is valid because it contains one @,
alice is alphanumeric, and example.com starts with a letter and ends with .com.

bob_at_example.com is invalid because it contains an underscore instead of an @.

charlie@example.net is invalid because the domain does not end with .com.

david@domain.com is valid because it meets all criteria.

eve@invalid is invalid because the domain does not end with .com.
Result table is ordered by user_id in ascending order.

My solution
Easy Python solution for Problem 3436 https://leetcode.com/problems/find-valid-emails/solutions/6351605/easy-python-solution-for-problem-3436-by-1971/
Intuition
Consistently check the conditions
"""
import pandas as pd

# Runtime 513 ms Beats 100.00%
# Memory 65.15 MB Beats 100.00%
# Time Complexity O(N∗M)
# Space Complexity O(N)

validc='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_'
def find_valid_emails2(users: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(columns=['user_id','email'])
    for index, row in users.iterrows():
        mail=row['email']
        if mail.count('@')==1:
            if mail.endswith('.com'):
                s=mail.split('@')
                aft=s[1].split('.')
                if aft[0].isalpha():
                    if all(s in validc for s in s[0]):
                        res = res._append(row)
    return res

# Wrong Answer - 7 / 11 testcases passed
def find_valid_emails2(users: pd.DataFrame) -> pd.DataFrame:
    res = pd.DataFrame(columns=['user_id','email'])
    for index, row in users.iterrows():
        mail=row['email']
        if mail.count('@')==1:
            if mail.endswith('.com'):
                s=mail.split('@')
                aft=s[1].split('.')
                if aft[0].isalpha():
                    if s[0][0] in validc:
                        if s[0][1:].isidentifier():
                            res = res._append(row)
    return res




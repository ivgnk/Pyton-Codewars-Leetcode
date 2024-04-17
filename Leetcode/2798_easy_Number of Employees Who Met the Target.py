"""
2798. Number of Employees Who Met the Target
https://leetcode.com/problems/number-of-employees-who-met-the-target/description/

There are n employees in a company, numbered from 0 to n - 1.
Each employee i has worked for hours[i] hours in the company.
The company requires each employee to work for at least target hours.
You are given a 0-indexed array of non-negative integers hours of length n and a non-negative integer target.
Return the integer denoting the number of employees who worked at least target hours.
"""

# Runtime 16 ms Beats 91.90% of users with Python
# Memory 11.68 MB Beats 37.01% of users with Python

def numberOfEmployeesWhoMetTarget(hours, target):
    """
    :type hours: List[int]
    :type target: int
    :rtype: int
    """
    return sum([1 for i in range(len(hours)) if hours[i]>=target])
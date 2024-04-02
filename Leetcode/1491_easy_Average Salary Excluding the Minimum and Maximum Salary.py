'''
1491. Average Salary Excluding the Minimum and Maximum Salary
You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary.
Answers within 10-5 of the actual answer will be accepted.

Example 1:
Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
'''

# Runtime 10 ms Beats 88.56% of users with Python
# Memory 11.48 MB Beats 95.02% of users with Python

def average(salary):
    """
    :type salary: List[int]
    :rtype: float
    """
    return (sum(salary) - min(salary) - max(salary)) / (len(salary) - 2.0)
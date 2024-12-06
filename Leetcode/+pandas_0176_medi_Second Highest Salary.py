"""
06.12.2024. Topics: Database
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

Table: Employee

+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest distinct salary from the Employee table.
If there is no second highest salary, return null (return None in Pandas).
The result format is in the following example.

Example 1:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| 200                 |
+---------------------+

Example 2:
Input:
Employee table:
+----+--------+
| id | salary |
+----+--------+
| 1  | 100    |
+----+--------+
Output:
+---------------------+
| SecondHighestSalary |
+---------------------+
| null                |
+---------------------+
"""

import pandas as pd
# Runtime 298 ms Beats 89.60%
# Memory 66.81 MB Beats 95.59%
# Runtime 338 ms Beats 67.95%
# Memory 66.26 MB Beats 99.38%
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sal = sorted(employee['salary'].unique())[::-1]
    if  len(sal) > 1:
        sal2 = sal[1]
    else :
        sal2 = float('nan')
    return pd.DataFrame([sal2], columns = ['SecondHighestSalary'])

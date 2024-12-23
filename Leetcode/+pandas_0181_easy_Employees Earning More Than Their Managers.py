"""
23.12.2024. Topics: Database
181. Employees Earning More Than Their Managers
https://leetcode.com/problems/employees-earning-more-than-their-managers/description/

SQL Schema
Pandas Schema
Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

Write a solution to find the employees who earn more than their managers.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Employee table:
+----+-------+--------+-----------+
| id | name  | salary | managerId |
+----+-------+--------+-----------+
| 1  | Joe   | 70000  | 3         |
| 2  | Henry | 80000  | 4         |
| 3  | Sam   | 60000  | Null      |
| 4  | Max   | 90000  | Null      |
+----+-------+--------+-----------+
Output:
+----------+
| Employee |
+----------+
| Joe      |
+----------+
Explanation: Joe is the only employee who earns more than his manager.
"""

# Runtime 282 ms Beats 97.17%
# Memory 68.14 MB Beats 75.5
import pandas as pd
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    manager = employee[['id', 'salary']].rename(columns={'id':'managerId', 'salary':'managerSalary'})
    df = pd.merge(employee, manager, how='left', on='managerId')
    df = df[df['salary'] > df['managerSalary']][['name']].rename(columns={'name':'Employee'})
    return df

def find_employees2(employee):
    merged = employee.merge(employee, left_on = "managerId", right_on = "id", suffixes = ('_emp', '_mgr'))
    s = merged[merged['salary_emp'] > merged['salary_mgr']]
    result = s[['name_emp']].rename(columns = {'name_emp' : 'Employee'})
    return result

def find_employees3(employee: pd.DataFrame) -> pd.DataFrame:
    managers = employee.rename(columns={'salary': 'manager_salary'})
    df_result = pd.merge(left=employee, right=managers, left_on='managerId', right_on='id', how='left')
    return df_result[df_result['salary'] > df_result['manager_salary']][['name_x']].rename(columns={'name_x': 'Employee'})
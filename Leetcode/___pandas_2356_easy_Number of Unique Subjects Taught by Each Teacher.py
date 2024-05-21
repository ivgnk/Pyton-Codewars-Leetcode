"""
Done 21.05.2024. Topics: Pandas, Database
2356. Number of Unique Subjects Taught by Each Teacher
https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/

Table: Teacher

+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.


Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.

The result format is shown in the following example.

Example 1:
Input:
Teacher table:
+------------+------------+---------+
| teacher_id | subject_id | dept_id |
+------------+------------+---------+
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
+------------+------------+---------+
Output:
+------------+-----+
| teacher_id | cnt |
+------------+-----+
| 1          | 2   |
| 2          | 4   |
+------------+-----+
Explanation:
Teacher 1:
  - They teach subject 2 in departments 3 and 4.
  - They teach subject 3 in department 3.
Teacher 2:
  - They teach subject 1 in department 1.
  - They teach subject 2 in department 1.
  - They teach subject 3 in department 1.
  - They teach subject 4 in department 1.
"""

import pandas as pd

# Runtime 852 ms Beats 5.24% of users with Pandas
# Memory 66.96 MB Beats 55.09% of users with Pandas

def count_unique_subjects3(teacher: pd.DataFrame) -> pd.DataFrame:
    teach= pd.DataFrame(columns=['teacher_id','cnt'])
    # https://pythonru.com/primery/pandas-value-counts
    teacher_id = teacher['teacher_id'].unique()
    for i in teacher_id:
        # https://www.geeksforgeeks.org/how-to-set-cell-value-in-pandas-dataframe/
        teach.at[i,'teacher_id']=i
        t = teacher[teacher['teacher_id'] == i]
        # https://favtutor.com/blogs/pandas-unique-values-in-column
        teach.at[i,'cnt'] = len(t['subject_id'].unique())
    return teach


# https://leetcode.com/problems/number-of-unique-subjects-taught-by-each-teacher/solutions/3851108/pandas-groupby-reset-index-nunique/

def count_unique_subjects2(teacher: pd.DataFrame) -> pd.DataFrame:
    df = teacher.groupby('teacher_id')['subject_id'].nunique().reset_index()
    df.columns = ['teacher_id', 'cnt']
    return df

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'teacher_id': sorted(teacher['teacher_id'].unique()),
        'cnt': teacher.groupby('teacher_id')['subject_id'].nunique()
    })
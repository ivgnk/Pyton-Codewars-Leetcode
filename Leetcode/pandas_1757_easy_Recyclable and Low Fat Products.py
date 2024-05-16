"""
Done 16.05.2024. Topics: Pandas, Database
1757. Recyclable and Low Fat Products
https://leetcode.com/problems/recyclable-and-low-fat-products/description/

Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
low_fats is an ENUM (category) of type ('Y', 'N') where 'Y' means this product is low fat and 'N' means it is not.
recyclable is an ENUM (category) of types ('Y', 'N') where 'Y' means this product is recyclable and 'N' means it is not.


Write a solution to find the ids of products that are both low fat and recyclable.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Products table:
+-------------+----------+------------+
| product_id  | low_fats | recyclable |
+-------------+----------+------------+
| 0           | Y        | N          |
| 1           | Y        | Y          |
| 2           | N        | Y          |
| 3           | Y        | Y          |
| 4           | N        | N          |
+-------------+----------+------------+
Output:
+-------------+
| product_id  |
+-------------+
| 1           |
| 3           |
+-------------+
Explanation: Only products 1 and 3 are both low fat and recyclable.
"""
# Runtime 668 ms Beats 47.56% of users with Pandas
# Memory 65.73 MB Beats 78.86% of users with Pandas

import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    # 1 https://www.codecamp.ru/blog/pandas-select-rows-based-on-column-values/
    # 2 geeksforgeeks.org/how-to-select-rows-from-a-dataframe-based-on-column-values/
    df_new = products.loc[(products['low_fats']=="Y") and (products['recyclable']=="Y")]
    return df_new
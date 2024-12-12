"""
12.12.2024. Topics: Database
183. Customers Who Never Order
https://leetcode.com/problems/customers-who-never-order/description/

Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

Write a solution to find all customers who never order anything.

Return the result table in any order.

The result format is in the following example.

Example 1:
Input:
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Output:
+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+
"""
# Runtime 504 ms Beats 5.15%
# Memory 66.34 MB Beats 99.26%
import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(customers,orders, how='left',left_on='id',right_on='customerId')
    result=result[result['customerId'].isna()][['name']]
    return result.rename(columns={'name':'Customers'})

def find_customers2(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result_df = customers[~customers['id'].isin(orders['customerId'])][['name']].rename(columns={'name':'Customers'})
    return result_df

# Runtime 443 ms Beats 18.61%
# Memory 67.03 MB Beats 92.50%
def find_customers3(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    ordered_customers = orders["customerId"].unique()
    # why we need unique() ?
    no_orders = customers[~customers["id"].isin(ordered_customers)]

    result = no_orders[["name"]].rename(columns={"name": "Customers"})
    return result

def find_customers4(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    result = customers[~customers['id'].isin(orders['customerId'])][['name']]
    result = result.rename(columns={'name': 'Customers'})
    return result
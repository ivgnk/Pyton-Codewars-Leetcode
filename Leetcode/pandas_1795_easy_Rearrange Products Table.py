"""
Done 22.05.2024. Topics: Pandas, Database
1795. Rearrange Products Table
https://leetcode.com/problems/rearrange-products-table/description/

Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

Write a solution to rearrange the Products table so that each row has (product_id, store, price).
If a product is not available in a store, do not include a row with that product_id and store combination in the result table.
Return the result table in any order.
The result format is in the following example.

Example 1:
Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
+------------+--------+--------+--------+
Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 0          | store1 | 95    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store1 | 70    |
| 1          | store3 | 80    |
+------------+--------+-------+
Explanation:
Product 0 is available in all three stores with prices 95, 100, and 105 respectively.
Product 1 is available in store1 with price 70 and store3 with price 80. The product is not available in store2.
"""

import pandas as pd

def set_pandas():
    ncn = ['product_id', 'store1', 'store2', 'store3']
    p2 = pd.DataFrame(columns=ncn); d=dict.fromkeys(ncn,0)
    d['product_id'] =0
    d['store1'] = 95
    d['store2'] = 100
    d['store3'] = 105
    p2 = p2._append(d, ignore_index=True)
    d['product_id'] = 1
    d['store1'] = 70
    d['store2'] = None
    d['store3'] = 80
    p2 = p2._append(d, ignore_index=True)
    return p2


# https://sky.pro/media/sozdanie-dataframe-v-pandas-putem-postrochnogo-dobavleniya/
# https/www.geeksforgeeks.org/how-to-add-one-row-in-an-existing-pandas-dataframe/

# Runtime 2444 ms Beats 5.02% of users with Pandas
# Memory 66.31 MB Beats 49.71% of users with Pandas

def rearrange_products_table2(products: pd.DataFrame) -> pd.DataFrame:
    ncn=['product_id','store','price']
    p2=pd.DataFrame(columns=ncn)
    cols=list(products); d=dict.fromkeys(ncn,0)
    for i in range(len(products)):
        d['product_id'] = products.iloc[i]['product_id']
        for nm in cols[1:]:
            d['store']=nm
            d['price']=products.iloc[i][nm]
            if pd.notna(d['price']):
                p2=p2._append(d, ignore_index=True)
    return p2


# https://leetcode.com/problems/rearrange-products-table/solutions/3863397/pandas-simple-easy-to-understand/
# Runtime 735 ms Beats 42.92% of users with Pandas
# Memory 65.62 MB Beats 85.60% of users with Pandas
# Runtime 552 ms Beats 99.42% of users with Pandas
# Memory 65.59 MB Beats 86.92% of users with Pandas
def rearrange_products_table3(products: pd.DataFrame) -> pd.DataFrame:
    # Create an empty list to store the rearranged rows
    r2 = []
    # Iterate over each row in the original table
    for _, row in products.iterrows():
        product_id = row['product_id']
        # Check each store for price availability
        for store_col in ['store1', 'store2', 'store3']:
            price = row[store_col]
            if pd.notna(price):
                # If the price is not null, add the (product_id, store, price) tuple to the list
                r2.append((product_id, store_col, price))

    # Create a new DataFrame with the rearranged rows
    result_table = pd.DataFrame(r2, columns=['product_id', 'store', 'price'])

    return result_table

p2=set_pandas()
print(rearrange_products_table(p2))
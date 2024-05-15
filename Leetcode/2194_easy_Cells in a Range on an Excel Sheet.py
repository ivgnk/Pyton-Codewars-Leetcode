"""
Done 16.05.2024. Topics: String
2194. Cells in a Range on an Excel Sheet

A cell (r, c) of an excel sheet is represented as a string "<col><row>" where:
<col> denotes the column number c of the cell. It is represented by alphabetical letters.
For example, the 1st column is denoted by 'A', the 2nd by 'B', the 3rd by 'C', and so on.
<row> is the row number r of the cell. The rth row is represented by the integer r.
You are given a string s in the format "<col1><row1>:<col2><row2>",
where <col1> represents the column c1, <row1> represents the row r1,
<col2> represents the column c2, and <row2> represents the row r2, such that r1 <= r2 and c1 <= c2.

Return the list of cells (x, y) such that r1 <= x <= r2 and c1 <= y <= c2.
The cells should be represented as strings in the format mentioned above and be sorted
in non-decreasing order first by columns and then by rows.

Example 1:
Input: s = "K1:L2"
Output: ["K1","K2","L1","L2"]
Explanation:
The above diagram shows the cells which should be present in the list.
The red arrows denote the order in which the cells should be presented.

Example 2:
Input: s = "A1:F1"
Output: ["A1","B1","C1","D1","E1","F1"]
Explanation:
The above diagram shows the cells which should be present in the list.
The red arrow denotes the order in which the cells should be presented.

Hint 1
From the given string, find the corresponding rows and columns.
Hint 2
Iterate through the columns in ascending order and for each column,
iterate through the rows in ascending order to obtain the required cells in sorted order.
"""

# Runtime 19 ms Beats 72.93% of users with Python
# Memory 11.76 MB Beats 43.65% of users with Python

NC='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def cellsInRange(s):
    """
    :type s: str
    :rtype: List[str]
    """
    fc=s[0];      lc=s[3]
    fn=int(s[1]); ln=int(s[4])
    cols=[s for s in NC if s>=fc and s<=lc]
    rows=[i for i in range(fn,ln+1)]
    # print(cols)
    # print(rows)
    return [c+str(r) for c in cols for r in rows]

print(cellsInRange("K1:L2"))
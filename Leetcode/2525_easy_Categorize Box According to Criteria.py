"""
Done 12.05.2024. Topics: Math
Given four integers length, width, height, and mass, representing the dimensions and mass of a box,
respectively, return a string representing the category of the box.

The box is "Bulky" if: Any of the dimensions of the box is greater or equal to 104.
Or, the volume of the box is greater or equal to 109.

If the mass of the box is greater or equal to 100, it is "Heavy".

If the box is both "Bulky" and "Heavy", then its category is "Both".

If the box is neither "Bulky" nor "Heavy", then its category is "Neither".

If the box is "Bulky" but not "Heavy", then its category is "Bulky".

If the box is "Heavy" but not "Bulky", then its category is "Heavy".

Note that the volume of the box is the product of its length, width and height.

Example 1:
Input: length = 1000, width = 35, height = 700, mass = 300
Output: "Heavy"
Explanation:
None of the dimensions of the box is greater or equal to 104.
Its volume = 24500000 <= 109. So it cannot be categorized as "Bulky".
However mass >= 100, so the box is "Heavy".
Since the box is not "Bulky" but "Heavy", we return "Heavy".

Example 2:
Input: length = 200, width = 50, height = 800, mass = 50
Output: "Neither"
Explanation:
None of the dimensions of the box is greater or equal to 104.
Its volume = 8 * 106 <= 109. So it cannot be categorized as "Bulky".
Its mass is also less than 100, so it cannot be categorized as "Heavy" either.
Since its neither of the two above categories, we return "Neither".
"""

# Runtime 7 ms Beats 92.31% of users with Python
# Memory 11.71 MB Beats 18.46% of users with Python

def categorizeBox(length, width, height, mass):
    """
    :type length: int
    :type width: int
    :type height: int
    :type mass: int
    :rtype: str
    """
    n104=10**4; n109=10**9
    rs=""; rm=""; res=""
    if length>=n104 or width>=n104 or height>=n104 or length*width*height>=n109: rs="Bulky"
    if mass>=100: rm="Heavy"
    if rs=="Bulky" and rm=="Heavy": res="Both"
    if rs != "Bulky" and rm != "Heavy": res="Neither"

    if rs=="Bulky" and rm!="Heavy": res="Bulky"
    if rs!="Bulky" and rm=="Heavy": res="Heavy"
    return res


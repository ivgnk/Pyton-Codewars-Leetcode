"""
Done 09.05.2024. Topics: Array, Greedy, Sorting
1710. Maximum Units on a Truck

You are assigned to put some amount of boxes onto one truck.
You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:
Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.

Example 2:
Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91

Hint 1
If we have space for at least one box, it's always optimal to put the box with the most units.
Hint 2
Sort the box types with the number of units per box non-increasingly.
Hint 3
Iterate on the box types and take from each type as many as you can.
"""

# Runtime 112 ms Beats 58.68% of users with Python
# Memory 12.02 MB Beats 88.02% of users with Python

def maximumUnits(boxTypes, truckSize):
    """
    :type boxTypes: List[List[int]]
    :type truckSize: int
    :rtype: int
    """
    boxTypes=sorted(boxTypes, key=lambda x: -x[1])
    i=-1; sb=0; su=0
    while sb<truckSize and i<len(boxTypes)-1:
        i=i+1
        if sb+boxTypes[i][0]<=truckSize:
            sb=sb+boxTypes[i][0]
            su=su+boxTypes[i][0]*boxTypes[i][1]
        else:
            nn = truckSize-sb
            sb=sb+nn
            su = su + nn * boxTypes[i][1]
    return su



print(maximumUnits(boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4))


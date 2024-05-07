"""
Done 07.05.2024. Topics: Array, Simulation
2960. Count Tested Devices After Test Operations
https://leetcode.com/problems/count-tested-devices-after-test-operations/description/

You are given a 0-indexed integer array batteryPercentages having length n,
denoting the battery percentages of n 0-indexed devices.
Your task is to test each device i in order from 0 to n - 1,
by performing the following test operations:
- If batteryPercentages[i] is greater than 0:
-- Increment the count of tested devices.
-- Decrease the battery percentage of all devices with indices j in the range [i + 1, n - 1] by 1, ensuring their battery percentage never goes below 0, i.e, batteryPercentages[j] = max(0, batteryPercentages[j] - 1).
-- Move to the next device.
- Otherwise, move to the next device without performing any test.

Return an integer denoting the number of devices that will be tested after performing the test operations in order.

Example 1:
Input: batteryPercentages = [1,1,2,1,3]
Output: 3
Explanation: Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] > 0, so there is now 1 tested device, and batteryPercentages becomes [1,0,1,0,2].
At device 1, batteryPercentages[1] == 0, so we move to the next device without testing.
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages becomes [1,0,1,0,1].
At device 3, batteryPercentages[3] == 0, so we move to the next device without testing.
At device 4, batteryPercentages[4] > 0, so there are now 3 tested devices, and batteryPercentages stays the same.
So, the answer is 3.

Example 2:
Input: batteryPercentages = [0,1,2]
Output: 2
Explanation: Performing the test operations in order starting from device 0:
At device 0, batteryPercentages[0] == 0, so we move to the next device without testing.
At device 1, batteryPercentages[1] > 0, so there is now 1 tested device, and batteryPercentages becomes [0,1,1].
At device 2, batteryPercentages[2] > 0, so there are now 2 tested devices, and batteryPercentages stays the same.
So, the answer is 2.
"""

# Runtime 87 ms Beats 7.82% of users with Python
# Memory 22.96 MB Beats 8.94% of users with Python
import numpy as np
def countTestedDevices2(batteryPercentages):
    """
    :type batteryPercentages: List[int]
    :rtype: int
    """
    b=np.array(batteryPercentages)
    n=0; ll=len(batteryPercentages)
    for i in range(ll):
        if b[i]>0:
           b[i+1:]=b[i+1:]-1
           n=n+1
    return n

# Runtime 65 ms Beats 41.90% of users with Python
# Memory 11.66 MB Beats 37.43% of users with Python
def countTestedDevices3(batteryPercentages):
    n=0; ll=len(batteryPercentages)
    for i in range(ll):
        if batteryPercentages[i]>0:
            batteryPercentages[i+1:]=list(map(lambda x: x-1, batteryPercentages[i+1:]))
            n=n+1
    return n

# Runtime 62 ms Beats 46.93% of users with Python
# Memory 11.65 MB Beats 37.43% of users with Python
def countTestedDevices(batteryPercentages):
    for i in range(len(batteryPercentages)):
        if batteryPercentages[i]>0:
            batteryPercentages[i+1:]=list(map(lambda x: x-1, batteryPercentages[i+1:]))
    return sum(i>0 for i in batteryPercentages)

print(countTestedDevices([1,1,2,1,3]))

"""
Done 13.05.2024. Topics: Array, Sorting

You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
Each people[i] = [hi, ki] represents the ith person of height hi
with exactly ki other people in front who have a height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people.
The returned queue should be formatted as an array queue, where queue[j] = [hj, kj]
is the attributes of the jth person in the queue (queue[0] is the person at the front of the queue).

Example 1:
Input: people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Output: [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
Explanation:
Person 0 has height 5 with no other people taller or the same height in front.
Person 1 has height 7 with no other people taller or the same height in front.
Person 2 has height 5 with two persons taller or the same height in front, which is person 0 and 1.
Person 3 has height 6 with one person taller or the same height in front, which is person 1.
Person 4 has height 4 with four people taller or the same height in front, which are people 0, 1, 2, and 3.
Person 5 has height 7 with one person taller or the same height in front, which is person 1.
Hence [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] is the reconstructed queue.

Example 2:
Input: people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
Output: [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]

Hint 1
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?
Hint 2
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
"""

# from https://www.mo4tech.com/leetcode-406-queue-reconstruction-by-height-python.html
# Runtime 70 ms Beats 29.91% of users with Python
# Memory 12.25 MB Beats 40.17% of users with Python
# Runtime 66 ms Beats 41.88% of users with Python
# Memory 12.48 MB Beats 17.09% of users with Python
# Runtime 60 ms Beats 77.78% of users with Python
# Memory 12.30 MB Beats 40.17% of users with Python

# also 1 https://programmersought.com/article/86957163595/
# also 2 https://www.youtube.com/watch?v=eOeZcJN0HKc
# also 3 https://medium.com/@codeandnotes/leetcode-406-queue-reconstruction-by-height-2f9e81a03f2

def reconstructQueue(people):
    """
    :type people: List[List[int]]
    :rtype: List[List[int]]
    """
    res = []
    e = sorted(people, key=lambda x: (-x[0], x[1]))
    # print(e,type(e))
    for h, k in e :
        res.insert(k, [h,k])
        # print(h, k, res )
    return res

print(reconstructQueue([[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]])) # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]
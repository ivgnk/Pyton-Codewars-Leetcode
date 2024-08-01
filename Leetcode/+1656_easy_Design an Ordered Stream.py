"""
01.08.2024. Topics: Array
1656. Design an Ordered Stream
https://leetcode.com/problems/design-an-ordered-stream/

There is a stream of n (idKey, value) pairs arriving in an arbitrary order,
where idKey is an integer between 1 and n and value is a string.
No two pairs have the same id.

Design a stream that returns the values in increasing order of their IDs by returning
a chunk (list) of values after each insertion.
The concatenation of all the chunks should result in a list of the sorted values.

Implement the OrderedStream class:
OrderedStream(int n) Constructs the stream to take n values.
String[] insert(int idKey, String value) Inserts the pair (idKey, value) into the stream,
then returns the largest possible chunk of currently inserted values that appear next in the order.

Example:
Input
["OrderedStream", "insert", "insert", "insert", "insert", "insert"]
[[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]
Output
[null, [], ["aaaaa"], ["bbbbb", "ccccc"], [], ["ddddd", "eeeee"]]

Explanation
// Note that the values ordered by ID is ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"].
OrderedStream os = new OrderedStream(5);
os.insert(3, "ccccc"); // Inserts (3, "ccccc"), returns [].
os.insert(1, "aaaaa"); // Inserts (1, "aaaaa"), returns ["aaaaa"].
os.insert(2, "bbbbb"); // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
os.insert(5, "eeeee"); // Inserts (5, "eeeee"), returns [].
os.insert(4, "ddddd"); // Inserts (4, "ddddd"), returns ["ddddd", "eeeee"].
// Concatentating all the chunks returned:
// [] + ["aaaaa"] + ["bbbbb", "ccccc"] + [] + ["ddddd", "eeeee"] = ["aaaaa", "bbbbb", "ccccc", "ddddd", "eeeee"]
// The resulting order is the same as the order above.


Constraints:
1 <= n <= 1000
1 <= id <= n
value.length == 5
value consists only of lowercase letters.
Each call to insert will have a unique id.
Exactly n calls will be made to insert.

Hint 1
Maintain the next id that should be outputted.
Hint 2
Maintain the ids that were inserted in the stream.
Hint 3
Per each insert, make a loop where you check if the id that has the turn has been inserted,
and if so increment the id that has the turn and continue the loop, else break.
"""

# https://leetcode.com/problems/design-an-ordered-stream/solutions/2519324/python3-runtime-faster-than-90-82-memory-less-than-93-18-testing/
# More Explanations
# https://leetcode.com/problems/design-an-ordered-stream/description/comments/1807584
# https://leetcode.com/problems/design-an-ordered-stream/description/comments/2247396
# https://leetcode.com/problems/design-an-ordered-stream/description/comments/2374550
# https://leetcode.com/problems/design-an-ordered-stream/description/comments/2415155

# Runtime 137 ms Beats 100.00%
# Memory 12.26 MB Beats 42.17%

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.lst = [None] * (n+1)
        self.ptr = 0

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey - 1] = value
        res = []

        while self.stream[self.i]:
            res.append(self.stream[self.i])
            self.i += 1
        return res

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
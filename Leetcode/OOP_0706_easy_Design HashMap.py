"""
Done 22.09.2024. Topics: Array, Hash Table
706. Design HashMap
https://leetcode.com/problems/design-hashmap/description/

Design a HashMap without using any built-in hash table libraries.
Implement the MyHashMap class:

MyHashMap() initializes the object with an empty map.
- void put(int key, int value) inserts a (key, value) pair into the HashMap.
If the key already exists in the map, update the corresponding value.
- int get(int key) returns the value to which the specified key is mapped,
or -1 if this map contains no mapping for the key.
- void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.

Example 1:
Input
["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
[[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
Output
[null, null, null, 1, -1, null, 1, null, -1]
Explanation
MyHashMap myHashMap = new MyHashMap();
myHashMap.put(1, 1); // The map is now [[1,1]]
myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
myHashMap.get(2);    // return -1 (i.e., not found), The map is now [[1,1]]

Constraints:
0 <= key, value <= 10**6
At most 10**4 calls will be made to put, get, and remove.
"""

# Runtime 169 ms Beats 66.11%
# Memory 14.77 MB Beats 59.93%
# Runtime 151 ms Beats 95.16%
# Memory 14.58 MB Beats 86.31%
class MyHashMap(object):

    def __init__(self):
        self.dd=dict()

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        self.dd[key]=value

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dd:
            return self.dd[key]
        else: return -1

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.dd:
            self.dd.pop(key)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
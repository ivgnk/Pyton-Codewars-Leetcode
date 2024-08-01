"""
Done 01.08.2024
2424. Longest Uploaded Prefix
https://leetcode.com/problems/longest-uploaded-prefix/


You are given a stream of n videos, each represented by a distinct number
from 1 to n that you need to "upload" to a server.
You need to implement a data structure that calculates the length of the longest uploaded prefix
at various points in the upload process.
We consider i to be an uploaded prefix if all videos in the range 1 to i (inclusive) have been uploaded to the server.
The longest uploaded prefix is the maximum value of i that satisfies this definition.

Implement the LUPrefix class:
LUPrefix(int n) Initializes the object for a stream of n videos.
void upload(int video) Uploads video to the server.
int longest() Returns the length of the longest uploaded prefix defined above.

Example 1:
Input
["LUPrefix", "upload", "longest", "upload", "longest", "upload", "longest"]
[[4], [3], [], [1], [], [2], []]
Output
[null, null, 0, null, 1, null, 3]

Explanation
LUPrefix server = new LUPrefix(4);   // Initialize a stream of 4 videos.
server.upload(3);                    // Upload video 3.
server.longest();                    // Since video 1 has not been uploaded yet, there is no prefix.
                                     // So, we return 0.
server.upload(1);                    // Upload video 1.
server.longest();                    // The prefix [1] is the longest uploaded prefix, so we return 1.
server.upload(2);                    // Upload video 2.
server.longest();                    // The prefix [1,2,3] is the longest uploaded prefix, so we return 3.


Constraints:
1 <= n <= 10**5
1 <= video <= n
All values of video are distinct.
At most 2 * 105 calls in total will be made to upload and longest.
At least one call will be made to longest.

Hint 1
Maintain an array keeping track of whether video “i” has been uploaded yet.
"""

# Runtime 480 ms Beats 83.33%
# Memory 74.88 MB Beats 33.33%

class LUPrefix(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.lst=[None]*(n+1)
        self.ind=0
        self.start=True

    def upload(self, video):
        """
        :type video: int
        :rtype: None
        """
        self.lst[video-1]=video

    def longest(self):
        """
        :rtype: int
        """
        if self.start:
            self.ind=0
            self.start=False

        i=self.ind
        while self.lst[i]:
            i=i+1
        if i==0:
            self.start=True
            return 0
        else:
            self.ind=i-1
            # print(self.lst)
            return self.lst[self.ind]

obj = LUPrefix(4)
obj.upload(3)
print(obj.longest())
obj.upload(1)
print(obj.longest())

# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()
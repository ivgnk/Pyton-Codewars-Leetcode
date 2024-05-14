"""
Done 14.05.2024. Topics: Hash Table, String, Design, Hash Function
535. Encode and Decode TinyURL
https://leetcode.com/problems/encode-and-decode-tinyurl/description/

Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as
https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk.
Design a class to encode a URL and decode a tiny URL.

There is no restriction on how your encode/decode algorithm should work.
You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.

Implement the Solution class:
Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl.
It is guaranteed that the given shortUrl was encoded by the same object.

Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
"""

#  https://dev.to/seanpgallivan/solution-encode-and-decode-tinyurl-4mji

# Runtime 15 ms Beats 65.41% of users with Python
# Memory 11.92 MB Beats 9.77% of users with Python


import string
import random
class Codec:
    codeDB, urlDB = dict(), dict()
    chars = string.ascii_letters + string.digits

    def getCode(self):
        code = ''.join(random.choice(self.chars) for i in range(6))
        return "http://tinyurl.com/" + code

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl in self.urlDB: return self.urlDB[longUrl]
        code = self.getCode()
        while code in self.codeDB: code = self.getCode()
        self.codeDB[code] = longUrl
        self.urlDB[longUrl] = code
        return code

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

                :type shortUrl: str
                :rtype: str
        """
        return self.codeDB[shortUrl]

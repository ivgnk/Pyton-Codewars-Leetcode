"""
Done 21.10.2024. Topics: Array, String
806. Number of Lines To Write String
https://leetcode.com/problems/number-of-lines-to-write-string/
You are given a string s of lowercase English letters and an array widths denoting
how many pixels wide each lowercase English letter is.
Specifically, widths[0] is the width of 'a', widths[1] is the width of 'b', and so on.

You are trying to write s across several lines, where each line is no longer than 100 pixels.
Starting at the beginning of s, write as many letters on the first line such that the total width does not exceed 100 pixels. Then, from where you stopped in s, continue writing as many letters as you can on the second line. Continue this process until you have written all of s.

Return an array result of length 2 where:
result[0] is the total number of lines.
result[1] is the width of the last line in pixels.

Example 1:
Input: widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10],
s = "abcdefghijklmnopqrstuvwxyz"
Output: [3,60]
Explanation: You can write s as follows:
abcdefghij  // 100 pixels wide
klmnopqrst  // 100 pixels wide
uvwxyz      // 60 pixels wide
There are a total of 3 lines, and the last line is 60 pixels wide.

Example 2:
Input: widths = [4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "bbbcccdddaaa"
Output: [2,4]
Explanation: You can write s as follows:
bbbcccdddaa  // 98 pixels wide
a            // 4 pixels wide
There are a total of 2 lines, and the last line is 4 pixels wide.

Constraints:
widths.length == 26
2 <= widths[i] <= 10
1 <= s.length <= 1000
s contains only lowercase English letters.

My solution https://leetcode.com/problems/number-of-lines-to-write-string/solutions/5947150/easy-python-solution-for-problem-0806-with-pre-defined-list/
Intuition
Cycle by letters and count string length

"""
# Runtime 7 ms Beats 98.70%
# Memory 11.83 MB Beats 18.18%
# Time Complexity O(N)
# Space Complexity O(1)
llst=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def numberOfLines(widths, s):
    """
    :type widths: List[int]
    :type s: str
    :rtype: List[int]
    """
    dd=dict(zip(llst,widths))
    # print(dd);
    ll=0; n=0
    for s1 in s:
        if ll+dd[s1]<=100:
            ll=ll + dd[s1]
        else:
            ll = dd[s1]
            n+=1
    if ll !=0: n+=1
    return [n,ll]

# print()
numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz")




print(numberOfLines(widths = [10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10], s = "abcdefghijklmnopqrstuvwxyz"))

# print({s:0 for s in list("abcdefghijklmnopqrstuvwxyz")})
# print(list("abcdefghijklmnopqrstuvwxyz"))

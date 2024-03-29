'''
1078. Occurrences After Bigram
https://leetcode.com/problems/occurrences-after-bigram/description/

Given two strings first and second, consider occurrences in some text of the form "first second third",
where second comes immediately after first, and third comes immediately after second.
Return an array of all the words third for each occurrence of "first second third".

Example 1:
Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

Example 2:
Input: text = "we will we will rock you", first = "we", second = "will"
Output: ["we","rock"]
'''

# Runtime 13 ms Beats 58.93% of users with Python
# Memory 11.82 MB Beats 11.61% of users with Python

def findOcurrences(text, first, second):
    """
    :type text: str
    :type first: str
    :type second: str
    :rtype: List[str]
    """
    res=[]
    str_list=text.split()
    for i in range(1,len(str_list)-1):
        if str_list[i-1]==first and str_list[i]==second:
            res.append(str_list[i+1])
    return res

print(findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))


"""
Done 04.06.2024. Topics: Hash Table, String, Greedy
409. Longest Palindrome
Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome  that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.
"""

# Runtime 17 ms Beats 58.22% of users with Python
# Memory 11.49 MB Beats 98.95% of users with Python

def longestPalindrome(s):
    """
    :type s: str
    :rtype: int
    """
    ll=len(s)
    if ll==1: return ll
    elif s==s[::-1]: return ll
    dd=dict()
    for i in range(ll):
        if s[i] in dd:
            dd[s[i]]=dd[s[i]]+1
        else:
            dd[s[i]]=1
    with1=False
    ssum=0
    for k, v in dd.items():
        if v%2==0:
            ssum = ssum + v
        else:
            if v%2 !=0 and not with1:
                with1=True
                ssum = ssum+1
            ssum = ssum + (v//2)*2
        print(' ',k,ssum)
    return ssum



print(longestPalindrome("jglknendplocymmvwtoxvebkekzfdhykknufqdkntnqvgfbahsljkobhbxkvyictzkqjqydczuxjkgecdyhixdttxfqmgksrkyvopwprsgoszftuhawflzjyuyrujrxluhzjvbflxgcovilthvuihzttzithnsqbdxtafxrfrblulsakrahulwthhbjcslceewxfxtavljpimaqqlcbrdgtgjryjytgxljxtravwdlnrrauxplempnbfeusgtqzjtzshwieutxdytlrrqvyemlyzolhbkzhyfyttevqnfvmpqjngcnazmaagwihxrhmcibyfkccyrqwnzlzqeuenhwlzhbxqxerfifzncimwqsfatudjihtumrtjtggzleovihifxufvwqeimbxvzlxwcsknksogsbwwdlwulnetdysvsfkonggeedtshxqkgbhoscjgpiel"))


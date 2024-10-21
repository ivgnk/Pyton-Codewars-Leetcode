"""
Done 21.10.2024. Topics, String
929. Unique Email Addresses
https://leetcode.com/problems/unique-email-addresses

Every valid email consists of a local name and a domain name, separated by the '@' sign.
Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address,
mail sent there will be forwarded to the same address without dots in the local name.
Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored.
This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i],
return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:
1 <= emails.length <= 100
1 <= emails[i].length <= 100
emails[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
Domain names end with the ".com" suffix.
Domain names must contain at least one character before ".com" suffix.

My solution https://leetcode.com/problems/unique-email-addresses/solutions/5947333/fast-3-ms-but-long-python-solution-for-problem-0929/
Fast (3 ms) , but long Python solution for Problem 0929
"""

# Runtime 3 ms Beats 99.82%
# Memory 16.88 MB Beats 5.35%
def numUniqueEmails(emails):
    """
    :type emails: List[str]
    :rtype: int
    """
    sset=set()
    for s in emails:
        if s.count('@')==1:
            locc, domm=s.split('@')
            if locc!='' and domm!='':
                if locc[0] !='+':
                    if domm.endswith(".com") and domm[0] !='.':
                        locc=locc.replace('.','')
                        if (frst:=locc.find('+'))>0:
                            locc=locc[:frst]
                        sset.add((domm,locc))
    return len(sset)

print(numUniqueEmails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))

print(numUniqueEmails(["a@leetcode.com","b@leetcode.com","c@leetcode.com"]))
"""
Done 05.10.2024. Topics: Hash Table, Two Pointers, Sorting
2491. Divide Players Into Teams of Equal Skill
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/

You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player.
Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams,
or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

Example 1:
Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation:
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.

Example 2:
Input: skill = [3,4]
Output: 12
Explanation:
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.

Example 3:
Input: skill = [1,1,2,3]
Output: -1
Explanation:
There is no way to divide the players into teams such that the total skill of each team is equal.

Constraints:
2 <= skill.length <= 105
skill.length is even.
1 <= skill[i] <= 1000

Hint 1
Try sorting the skill array.
Hint 2
It is always optimal to pair the weakest available player with the strongest available player.

Tip
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/description/comments/1705326
- sort the array

- As skill of each team is to be equal, we take target skill value to be smallest+largest in the array

- We pick the smallest element in the array and add the largest, check if this is equal to the target, if not, we immediately quit the program as we return -1
-
Else we add the product of the team into a variable

return the variable

My solution
https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/solutions/5870828/easy-python-solution-based-on-tip-in-first-comment-in-discussion/
✏️ Easy Python solution based on tip in first comment in discussion
many thanks to https://leetcode.com/u/aryan1113/
"""

# Runtime 405 ms Beats 91.04%
# Memory 22.48 MB Beats 85.07%
# Time Complexity O(NLogN)
# Space Complexity O(1)
def dividePlayers(skill):
    """
    :type skill: List[int]
    :rtype: int
    """
    skill.sort()
    target=skill[0]+skill[-1]
    prod=skill[0]*skill[-1]
    for i in range(1,len(skill)//2):
        if skill[i]+skill[-1-i]==target:
            prod +=skill[i]*skill[-1-i]
        else: return -1
    return prod

print(dividePlayers([3,2,5,1,3,4]))
print(dividePlayers([3,4]))
print(dividePlayers([1,1,2,3]))
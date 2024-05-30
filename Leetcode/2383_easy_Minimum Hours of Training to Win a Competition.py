"""
Done 30.05.2024. Topics: Array, Greedy

2383. Minimum Hours of Training to Win a Competition
https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/description/

You are entering a competition, and are given two positive integers initialEnergy and initialExperience
denoting your initial energy and initial experience respectively.

You are also given two 0-indexed integer arrays energy and experience, both of length n.

You will face n opponents in order. The energy and experience of the ith opponent is denoted by energy[i]
and experience[i] respectively. When you face an opponent,
you need to have both strictly greater experience and energy to defeat them and move to the next opponent if available.

Defeating the ith opponent increases your experience by experience[i], but decreases your energy by energy[i].

Before starting the competition, you can train for some number of hours.
After each hour of training, you can either choose to increase your initial experience by one,
or increase your initial energy by one.

Return the minimum number of training hours required to defeat all n opponents.

Example 1:
Input: initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]
Output: 8

Explanation: You can increase your energy to 11 after 6 hours of training, and your experience to 5 after 2 hours of training.
You face the opponents in the following order:
- You have more energy and experience than the 0th opponent so you win.
  Your energy becomes 11 - 1 = 10, and your experience becomes 5 + 2 = 7.
- You have more energy and experience than the 1st opponent so you win.
  Your energy becomes 10 - 4 = 6, and your experience becomes 7 + 6 = 13.
- You have more energy and experience than the 2nd opponent so you win.
  Your energy becomes 6 - 3 = 3, and your experience becomes 13 + 3 = 16.
- You have more energy and experience than the 3rd opponent so you win.
  Your energy becomes 3 - 2 = 1, and your experience becomes 16 + 1 = 17.
You did a total of 6 + 2 = 8 hours of training before the competition, so we return 8.
It can be proven that no smaller answer exists.

Example 2:
Input: initialEnergy = 2, initialExperience = 4, energy = [1], experience = [3]
Output: 0
Explanation: You do not need any additional energy or experience to win the competition, so we return 0.

Hint 1
Find the minimum number of training hours needed for the energy and experience separately, and sum the results.
Hint 2
Try to increase the energy and experience until you find how much is enough to win the competition.

Tips:
Calculate energy required first. Unlike experience required to defeat an opponent where you gain
experience when defeating someone, you simply just lose energy(simple subtraction)
as you face opponents. You only need energy.sum + 1 in terms of energy required.

Ensure your experience exceeds your opponent before adding their experience to your experience.
"""

from icecream import ic

# Runtime 22 ms Beats 62.50% of users with Python
# Memory 11.44 MB Beats 96.88% of users with Python

def minNumberOfHours(initialEnergy, initialExperience, energy, experience):
    """
    :type initialEnergy: int
    :type initialExperience: int
    :type energy: List[int]
    :type experience: List[int]
    :rtype: int
    """
    sum_e = sum(energy)+1
    add_e = sum_e-initialEnergy if initialEnergy<sum_e else 0
    add_exp1 = 0
    for dat in experience:
        if initialExperience<=dat:
            add_exp=dat-initialExperience+1
            initialExperience=initialExperience+add_exp+dat
            add_exp1 = add_exp1+add_exp
        else: initialExperience=initialExperience+dat
    return add_e+add_exp1

# Runtime 25 ms Beats 34.38% of users with Python
# Memory 11.46 MB Beats 96.88% of users with Python

# https://leetcode.com/problems/minimum-hours-of-training-to-win-a-competition/solutions/2456780/greedy-python-simple/
def minNumberOfHours2(initialEnergy, initialExperience, energy, experience):
    """
    :type initialEnergy: int
    :type initialExperience: int
    :type energy: List[int]
    :type experience: List[int]
    :rtype: int
    """
    req_energy, req_exp = 0, 0
    ini_energy = initialEnergy
    iexp = initialExperience
    for i,exp in enumerate(experience):
        if exp >= iexp:
            req_exp = max(req_exp, exp - iexp + 1)
        iexp += exp

    req_energy = sum(energy) + 1 - ini_energy
    if req_energy < 0:
        req_energy = 0
    return req_energy + req_exp


# ic(minNumberOfHours(initialEnergy = 5, initialExperience = 3, energy = [1,4,3,2], experience = [2,6,3,1]))
# ic(minNumberOfHours(initialEnergy = 94, initialExperience =70,
#                     energy = [58,47,100,71,47,6,92,82,35,16,50,15,42,5,2,45,22],
#                     experience = [77,83,99,76,75,66,58,84,44,98,70,41,48,7,10,61,28]))
ic(minNumberOfHours2(initialEnergy = 94, initialExperience = 70,
                    energy = [58,47,100,71,47,6,92,82,35,16,50,15,42,5,2,45,22],
                    experience = [77,83,99,76,75,66,58,84,44,98,70,41,48,7,10,61,28]))
ic(minNumberOfHours(initialEnergy = 94, initialExperience = 70,
                    energy = [58,47,100,71,47,6,92,82,35,16,50,15,42,5,2,45,22],
                    experience = [77,83,99,76,75,66,58,84,44,98,70,41,48,7,10,61,28]))




"""
05.01.2025. Topics: Array, String, Prefix Sum
2381. Shifting Letters II
You are given a string s of lowercase English letters and a 2D integer array shifts
where shifts[i] = [starti, endi, directioni].
For every i, shift the characters in s from the index starti to the index endi (inclusive)
forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet
(wrapping around so that 'z' becomes 'a').
Similarly, shifting a character backward means replacing it with the previous letter
in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.

Example 1:
Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

Example 2:
Input: s = "dztz", shifts = [[0,0,0],[1,1,1]]
Output: "catz"
Explanation: Firstly, shift the characters from index 0 to index 0 backward. Now s = "cztz".
Finally, shift the characters from index 1 to index 1 forward. Now s = "catz".

Constraints:
1 <= s.length, shifts.length <= 5 * 104
shifts[i].length == 3
0 <= starti <= endi < s.length
0 <= directioni <= 1
s consists of lowercase English letters.

Hint 1
Instead of shifting every character in each shift,
could you keep track of which characters are shifted and by how much across all shifts?
Hint 2
Try marking the start and ends of each shift, then perform a prefix sum of the shifts.
"""

# Runtime 95 ms Beats 46.15%
# Memory 30.02 MB Beats 46.15%

# https://leetcode.com/problems/shifting-letters-ii/editorial/
def shiftingLetters(s, shifts):
    """
    :type s: str
    :type shifts: List[List[int]]
    :rtype: str
    """
    n = len(s)
    diff_array = [0] * n  # Initialize a difference array with all elements set to 0
    # Process each shift operation
    for shift in shifts:
        if shift[2] == 1:  # If direction is forward (1)
            diff_array[shift[0]] += 1  # Increment at the start index
            if shift[1] + 1 < n:
                diff_array[
                    shift[1] + 1
                ] -= 1  # Decrement at the end+1 index
        else:  # If direction is backward (0)
            diff_array[shift[0]] -= 1  # Decrement at the start index
            if shift[1] + 1 < n:
                diff_array[
                    shift[1] + 1
                ] += 1  # Increment at the end+1 index

    result = list(s)
    number_of_shifts = 0

    # Apply the shifts to the string
    for i in range(n):
        number_of_shifts = (number_of_shifts + diff_array[i]) % 26  # Update cumulative shifts, keeping within the alphabet range
        if number_of_shifts < 0:
            number_of_shifts += 26  # Ensure non-negative shifts
        # Calculate the new character by shifting `s[i]`
        shifted_char = chr((ord(s[i]) - ord("a") + number_of_shifts) % 26 + ord("a"))
        result[i] = shifted_char

    return "".join(result)



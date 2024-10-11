"""
Done 11.10.2024. Topics: Array, Counting, Prefix Sum
1854. Maximum Population Year
https://leetcode.com/problems/maximum-population-year/description/

You are given a 2D integer array logs where each logs[i] = [birthi, deathi]
indicates the birth and death years of the ith person.

The population of some year x is the number of people alive during that year.
The ith person is counted in year x's population if x is in the inclusive range [birthi, deathi - 1].
Note that the person is not counted in the year that they die.

Return the earliest year with the maximum population.

Example 1:
Input: logs = [[1993,1999],[2000,2010]]
Output: 1993
Explanation: The maximum population is 1, and 1993 is the earliest year with this population.

Example 2:
Input: logs = [[1950,1961],[1960,1971],[1970,1981]]
Output: 1960

Explanation:
The maximum population is 2, and it had happened in years 1960 and 1970.
The earlier year between them is 1960.

Constraints:
1 <= logs.length <= 100
1950 <= birthi < deathi <= 2050

Hint 1
For each year find the number of people whose birth_i ≤ year and death_i > year.
Hint 2
Find the maximum value between all years.

My solution https://leetcode.com/problems/maximum-population-year/solutions/5898952/super-lazy-python-solution-based-on-hints/
✏️ Super lazy Python solution, based on hints

Intuition
Program in order of actions

Approach
1) Find min & max years
2) Make dictionary with years
3) Cycle by people, fill in the dictionary by years
4) Cycle by people, find first year with max persons
"""

from icecream import ic

# Runtime 43 ms Beats 61.45%
# Memory 16.47 MB Beats 88.93%

# Runtime 40 ms Beats 79.68%
# Memory 16.66 MB Beats 19.40%

def maximumPopulation(logs):
    """
    :type logs: List[List[int]]
    :rtype: int
    """
    ma=-1; mi=3000
    for x1,x2 in logs:
        mi=min(x1,mi)
        ma=max(x2,ma)
    dd={i:0  for i in  range(mi,ma)}
    for x1, x2 in logs:
        for i in range(x1, x2):
            dd[i]+=1
    mma=max([v for k, v in dd.items()])
    for k, v in dd.items():
        if v==mma: return k

a= [[2006,2007],[2037,2038],[1971,1972],[1973,1974],[2001,2002],[1987,1988],[2044,2045],[1972,1973],
 [2043,2044],[1990,1991],[2028,2029],[1984,1985],[1974,1975],[2033,2034],[1977,1978],[2011,2012],
 [1967,1968],[1955,1956],[1980,1981],[2039,2040],[1983,1984],[2019,2020],[1996,1997],[1981,1982],
 [1991,1992],[1965,1966],[2009,2010],[2027,2028],[2025,2026],[2046,2047],[2013,2014],[1956,1957],
 [2045,2046],[1997,1998],[1986,1987],[1998,1999],[2010,2011],[2023,2024],[2018,2019],[1952,1953],
 [2038,2039],[1978,1979],[2012,2013],[1969,1970],[2003,2004],[1968,1969],[1989,1990],[1994,1995],
 [2024,2025],[2016,2017],[2032,2033],[1979,1980],[2022,2023],[2017,2018],[1954,1955],[1962,1963],
 [2015,2016],[2021,2022],[1988,1989],[2008,2009],[1999,2000],[2030,2031],[2036,2037],[2048,2049],
 [1951,1952],[1963,1964],[2014,2015],[1992,1993],[2007,2008],[2004,2005],[1964,1965],[2049,2050],
 [1960,1961],[2002,2003],[1970,1971],[1975,1976],[1995,1996],[1985,1986],[1993,1994],[2005,2006],
 [1976,1977],[1957,1958],[1982,1983],[2020,2021],[1966,1967],[1961,1962],[2040,2041],[2047,2048],
 [1953,1954],[1950,1951],[2041,2042],[1959,1960],[2035,2036],[2000,2001],[2029,2030],[2034,2035],
 [1958,1959],[2042,2043],[2031,2032],[2026,2027]]
ic(maximumPopulation(a))


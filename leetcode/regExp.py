'''
LeetCode 10. Regular Expression Matching
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:

'.' Matches any single character.​​​​
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).
Constraints:

1 <= s.length <= 20
1 <= p.length <= 30
s contains only lowercase English letters.
p contains only lowercase English letters, '.', and '*'.
It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.

Example 1: Input: s = "aa", p = "a" Output: false Explanation: "a" does not match the entire string "aa".
Example 2: Input: s = "aa", p = "a*" Output: true Explanation: '*' means zero or more of the precedeng element, 'a'. 
Therefore, by repeating 'a' once, it becomes "aa".
Example 3: Input: s = "ab", p = ".*" Output: true Explanation: ".*" means "zero or more (*) of any character (.)".
'''
class Solution(object):
    #Written by Copilot
    #Beats 5.94% of python3 submissions
    #Same as Approach 1: Recursion on Solution tab
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '.'}
        if len(p) >= 2 and p[1] == '*':
            return self.isMatch(s, p[2:]) or first_match and self.isMatch(s[1:], p)
        else:
            return first_match and self.isMatch(s[1:], p[1:])

# call the function
s = Solution()
result = s.isMatch("aa", "a")
print(result)

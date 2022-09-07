'''
LeetCode: 44 Wildcard Matching
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Example 1: Input: s = "aa", p = "a" Output: false 
Explanation: "a" does not match the entire string "aa".
Example 2: Input: s = "aa", p = "*" Output: true
Explanation: '*' matches any sequence.
Example 3: Input: s = "cb", p = "?a" Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


'''
class Solution(object):
    #First attempt written by Copilot = Failed
    #Input: "aa", "*" 
    #Output: false
    #Expected: True
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        first_match = bool(s) and p[0] in {s[0], '?'}
        if len(p) >= 2 and p[1] == '*':
            m = self.isMatch(s, p[2:])
            n = self.isMatch(s[1:], p)
            return m or first_match and n
        else:
            return first_match and self.isMatch(s[1:], p[1:])

    #Second Attemp = Success
    #Faster than 67.38% of python3 submissions
    #Used crtl + enter and looked for solution that did not look the same as
    #first attempt; most were the same as first attempt
    #Solution tab locked
    def isMatch2(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        # dp[i][j] = True if s[:i] matches p[:j]
        dp = [[False] * (p_len + 1) for _ in range(s_len + 1)]
        dp[0][0] = True
        for j in range(1, p_len + 1):
            dp[0][j] = p[j - 1] == '*' and dp[0][j - 1]
        for i in range(1, s_len + 1):
            for j in range(1, p_len + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j - 1] and (p[j - 1] == '?' or p[j - 1] == s[i - 1])
        return dp[-1][-1]

"""
LeetCode #30 Substring with Concatenation of All Words
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated substring in s is a substring that contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" 
are all concatenated strings. "acdbef" is not a concatenated substring because it is not the concatenation of any permutation of words.
Return the starting indices of all the concatenated substrings in s. You can return the answer in any order.

Constraints:
1 <= s.length <= 104
1 <= words.length <= 5000
1 <= words[i].length <= 30
s and words[i] consist of lowercase English letters.

Example 1: Input: s = "barfoothefoobarman", words = ["foo","bar"] Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoo" and "foobar" respectively. 
The output order does not matter.
Example 2: Input: s = "wordgoodgoodgoodbestword", words = ["word","good","best","word"] Output: []
Example 3: Input: s = "barfoofoobarthefoobarman", words = ["bar","foo","the"] Output: [6,9,12]

"""
class Solution:
    #First Copilot Solution = Failed
    #Input: "mississippi" ["is"]
    #Output: [1]
    #Expected: [1,4]
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        if len(words) == 1:
            return [s.find(words[0])]
        wordLength = len(words[0])
        wordsLength = len(words) * wordLength
        result = []
        for i in range(len(s) - wordsLength + 1):
            if self.checkWords(s, words, i, wordLength):
                result.append(i)
        return result

    def checkWords(self, s, words, i, wordLength):
        wordDict = {}
        for word in words:
            if word in wordDict:
                wordDict[word] += 1
            else:
                wordDict[word] = 1
        for j in range(i, i + len(words) * wordLength, wordLength):
            if s[j:j + wordLength] in wordDict:
                wordDict[s[j:j + wordLength]] -= 1
                if wordDict[s[j:j + wordLength]] == 0:
                    del wordDict[s[j:j + wordLength]]
            else:
                return False
        return True

    #Second Copilot Solution = Success
    #Using ctlr + enter to find another solution, picked the first one
    #Beats 12.83% of python3 submissions
    #Similar to Approach 1: Check all Indices Using Hash Table in Solution tab
    def findSubstring2(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wordLen = len(words[0])
        wordCount = len(words)
        wordDict = {}
        for word in words:
            if word not in wordDict:
                wordDict[word] = 1
            else:
                wordDict[word] += 1
        result = []
        for i in range(len(s) - wordCount * wordLen + 1):
            tempDict = {}
            for j in range(wordCount):
                word = s[i + j * wordLen : i + j * wordLen + wordLen]
                if word not in tempDict:
                    tempDict[word] = 1
                else:
                    tempDict[word] += 1
            if tempDict == wordDict:
                result.append(i)
        return result

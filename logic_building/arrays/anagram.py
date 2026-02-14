# https://neetcode.io/problems/is-anagram/question
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for item in s:
            if item in count:
                count[item] = count[item] + 1
            else:
                count[item] = 1
        
        for item in t:
            if item in count:
                count[item] = count[item] - 1
            else:
                return False
                
        for item in count:
            if count[item] != 0:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    s = "xx"
    t = 'xx'
    print(sol.isAnagram(s, t))

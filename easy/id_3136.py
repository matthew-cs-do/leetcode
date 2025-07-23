"""
    https://leetcode.com/problems/valid-word
"""


class Solution:
    def isValid(self, word: str) -> bool:
        if len(word) < 3:
            return False
        has_vowel = has_consonant = False
        vowels = "aiueo"
        for c in word.lower():
            if c.isalpha():
                if c in vowels:
                    has_vowel = True
                else:
                    has_consonant = True
            elif not c.isalnum():
                return False
        return has_vowel and has_consonant

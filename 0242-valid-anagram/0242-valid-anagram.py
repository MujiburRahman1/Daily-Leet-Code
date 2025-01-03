class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if string 't' is an anagram of string 's'.

        Args:
          s: The first string.
          t: The second string.

        Returns:
          True if 't' is an anagram of 's', False otherwise.
        """

        # If the lengths of the two strings are not equal, they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Create dictionaries to store the frequency of each character in both strings.
        count_s = {}  # Dictionary to store character counts for string 's'
        count_t = {}  # Dictionary to store character counts for string 't'

        # Count the frequency of each character in both strings.
        for char in s:  # Iterate through each character in string 's'
            count_s[char] = count_s.get(char, 0) + 1  # If the character is not in the dictionary, add it with a count of 1. Otherwise, increment its count.
        for char in t:  # Iterate through each character in string 't'
            count_t[char] = count_t.get(char, 0) + 1  # If the character is not in the dictionary, add it with a count of 1. Otherwise, increment its count.

        # If both dictionaries have the same key-value pairs (i.e., same character frequencies), then the strings are anagrams.
        return count_s == count_t
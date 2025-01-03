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
        if len(s) != len(t):  # Compare the lengths of the input strings 's' and 't'
            return False  # If the lengths are different, return False because they can't be anagrams

        # Create dictionaries to store the frequency of each character in both strings.
        countS, countT = {}, {}  # Initialize two empty dictionaries, countS for string 's' and countT for string 't'

        # Count the frequency of each character in both strings using a single loop.
        for i in range(len(s)):  # Iterate through the indices of the string 's' (since both strings have the same length)
            countS[s[i]] = 1 + countS.get(s[i], 0)  # Increment the count of the character s[i] in countS (if not present, initialize with 0 and then increment)
            countT[t[i]] = 1 + countT.get(t[i], 0)  # Increment the count of the character t[i] in countT (if not present, initialize with 0 and then increment)

        # If both dictionaries have the same key-value pairs (i.e., same character frequencies), then the strings are anagrams.
        return countS == countT  # Compare the two dictionaries. If they are equal, return True, otherwise return False.
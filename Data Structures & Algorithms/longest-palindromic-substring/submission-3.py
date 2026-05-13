class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The main idea that we go through each option and expand left and right
        # and check if char[left] == char[right]. If so, we continue the expansion
        # until we reach end. We need to be careful with even and odd length palindrome.

        if not s:
            return ""
        if len(s) == 1:
            return s
        if len(s) == 2:
            return s if s[0] == s[1] else s[0]

        longest_substring = ""

        def expand(left: int, right: int) -> str:

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            # Dont forget to revert the last loop!
            return s[left + 1 : right]

        # Now, we will do this
        for i in range(0, len(s) - 1):
            odd_length = expand(i, i)
            even_length = expand(i, i + 1)
            if len(odd_length) > len(longest_substring):
                longest_substring = odd_length
            if len(even_length) > len(longest_substring):
                longest_substring = even_length

        return longest_substring
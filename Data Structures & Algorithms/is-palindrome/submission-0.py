class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_s = "".join(char for char in s if char.isalnum()).casefold()
        l = 0
        r = len(normalized_s) - 1
        while l <= r :
            if normalized_s[l] != normalized_s[r]:
                return False
            l += 1
            r -= 1
        return True
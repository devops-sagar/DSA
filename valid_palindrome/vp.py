class Solution:
    def isPalindrome(self, s: str) -> bool:
        old = ''.join(filter(str.isalnum, s))
        new = old.lower()
        rev = new[::-1]
        if new == rev:
            return True
        else:
            return False
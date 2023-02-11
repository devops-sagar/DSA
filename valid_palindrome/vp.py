class Solution:
    def isPalindrome(self, s: str) -> bool:
        old = ''.join(filter(str.isalnum, s))
        new = old.lower()
        rev = new[::-1]
        if new == rev:
            return True
        else:
            return False

''' 
optimized solution:::::-----

class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s)-1

        while i != j and j >= i:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        
        return True


'''
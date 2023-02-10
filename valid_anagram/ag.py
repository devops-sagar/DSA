class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            print("False")
            return False
        else:
            if sorted(s) == sorted(t):
                print("True")
            else:
                print("False")

obj = Solution()
obj.isAnagram("abሴc", "bacሴ")
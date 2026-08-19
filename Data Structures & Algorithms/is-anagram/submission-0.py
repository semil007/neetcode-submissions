class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       sorted_text1 = "".join(sorted(s, key=str.lower))
       sorted_text2 = "".join(sorted(t, key=str.lower))
       if sorted_text1 == sorted_text2:
            return True
       else:
            return False
        
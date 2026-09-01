class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False

        characters = {c:0 for c in s}
        for c in s:
            characters[c] += 1

        for c in t:
            if c not in characters:
                return False
            characters[c] -= 1
            if characters[c] <0:
                return False

        return True
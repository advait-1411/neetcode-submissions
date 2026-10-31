class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False
        hashmap_s = Counter(s)

        for c in t:
            if c not in hashmap_s:
                return False
            hashmap_s[c] -= 1
            if hashmap_s[c] <0:
                return False
        return True

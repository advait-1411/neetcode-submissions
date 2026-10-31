class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        freq = Counter(nums)
        for f in freq :
            if freq[f] >1 :
                return True
        return False
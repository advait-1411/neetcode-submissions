class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= Counter(nums)
        ans = set()
        while k>0:
            max_freq= max(freq.values())
        # finding key using value of max frequency
            for key in freq:
                if freq[key] == max_freq:
                    ans.add(key)
                    freq.pop(key)
                    break
            k -= 1
        return list(ans)
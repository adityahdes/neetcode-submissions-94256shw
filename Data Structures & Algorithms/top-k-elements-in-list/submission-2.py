class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        a = set(nums)
        d = dict.fromkeys(a, 0)
        for val in a:
            d[val] = nums.count(val)
        return sorted(d, key=d.get, reverse=True)[:k]
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        snums = set(nums)
        for num in snums:
            if (num - 1) in snums:
                continue
            else:
                k = 1
                while(num + k in snums):
                    k += 1
                if k > longest:
                    longest = k
        return longest
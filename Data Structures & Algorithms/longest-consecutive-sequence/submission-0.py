class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        snums = set(nums)
        print(snums)
        for i in range(len(nums)):
            if (nums[i] - 1) in snums:
                continue
            else:
                k = 1
                while(True):
                    if nums[i] + k in snums:
                        k += 1
                    else:
                        break
                if k > longest:
                    longest = k
        return longest
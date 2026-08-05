class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            complement = target - nums[i]
            if(complement == nums[i] and nums.count(nums[i]) > 1):
                return [i, nums.index(complement, i+1)]
            elif(complement != nums[i] and nums.count(complement) > 0):
                return [i, nums.index(complement)]
            else:
                continue
        return [-1, -1]
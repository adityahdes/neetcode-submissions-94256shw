class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        checked_values = set(())
        nums.sort()
        i = 0
        while i < len(nums):
            if(nums[i] in checked_values):
                pass
            else:
                checked_values.add(nums[i])
                target = -nums[i]
                low = i + 1
                high = len(nums) - 1
                while(high > low):
                    temp = nums[low] + nums[high]
                    if temp == target:
                        triple = [nums[i], nums[low], nums[high]]
                        if triple not in out:
                            out.append(triple)
                        low += 1
                        high -= 1
                    elif temp < target:
                        low += 1
                    else:
                        high -= 1
            i += 1
        return out


                



# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         low = 0
#         high = len(numbers) - 1
#         while(high > low):
#             temp = numbers[low] + numbers[high]
#             if temp == target:
#                 return [low + 1, high + 1]
#             elif temp < target:
#                 low += 1
#             else:
#                 high -= 1
#         return -1 

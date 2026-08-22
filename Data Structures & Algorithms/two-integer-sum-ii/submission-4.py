class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1
        while(high > low):
            temp = numbers[low] + numbers[high]
            if temp == target:
                return [low + 1, high + 1]
            elif temp < target:
                low += 1
            else:
                high -= 1
        return -1 

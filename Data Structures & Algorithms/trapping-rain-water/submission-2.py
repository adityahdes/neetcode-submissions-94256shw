class Solution:
    def trap(self, height: List[int]) -> int:
        prefix = [0] * len(height)
        suffix = [0] * len(height)
        prefix[0] = 0
        suffix[len(height) - 1] = 0
        for i in range(1, len(height)):
            prefix[i] = max(prefix[i - 1], height[i - 1])
            suffix[len(height) - 1 - i] = max(suffix[len(height) - i], height[len(height) - i])
        sum = 0
        for i in range(len(height)):
            water = (min(prefix[i], suffix[i]) - height[i])
            if water > 0: sum += water
        return sum
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        px = [None] * n
        sx = [None] * n
        p = 1
        s = 1
        for i in range(len(nums)):
            px[i] = p
            sx[n - i - 1] = s
            if i != 0:
                px[i] = px[i-1] * nums[i-1]
                sx[n - i - 1] = sx[n - i] * nums[n - i]
        return list(map(lambda x, y: x * y, px, sx))
        
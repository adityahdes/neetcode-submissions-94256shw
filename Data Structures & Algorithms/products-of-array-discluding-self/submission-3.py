class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        px = [1] * n
        sx = [1] * n
        p = 1
        s = 1
        for i in range(len(nums)):
            px[i] = p
            p = p * nums[i]
            sx[n - i - 1] = s
            s = s * nums[n - i - 1]
        return list(map(lambda x, y: x * y, px, sx))
        
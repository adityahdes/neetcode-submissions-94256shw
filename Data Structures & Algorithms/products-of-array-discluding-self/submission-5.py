class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        px = [1] * n
        sx = [1] * n
        p = 1
        s = 1
        for i in range(n):
            px[i] *= p
            p *= nums[i]
        for i in range(n -1, -1, -1):
            sx[i] *= s
            s *= nums[i]
        return list(map(lambda x, y: x * y, px, sx))
        
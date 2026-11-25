class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # 1回目：resに左側の積を入れる
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # 2回目：右から順に右側の積をかけていく
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]

        return res
        
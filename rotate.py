class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1 or k == 0: return  # 边界条件很重要
        if k > len(nums):
            k = k % len(nums)

        nums[:] = nums[-k:] + nums[0:len(nums) - k]

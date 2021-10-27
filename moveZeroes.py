class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #分两段数据，把不为0的找到之后，后面的用0补充
        # j=0
        # for i in range(len(nums)):
        #     if nums[i]!=0:
        #         nums[j]=nums[i]
        #         j+=1
        # for i in range(j,len(nums)):
        #     nums[i]=0
        #双指针
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        numslen = len(nums)
        k = k % numslen
        res = nums[-3:]+nums[:-3]
        for i in range(numslen):
            nums[i] = res[i]


nums = [1,2,3,4,5,6,7]
Solution().rotate(nums,3)

print(nums)

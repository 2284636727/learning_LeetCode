class Solution:
    def __init__(self):
        pass
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        match_dict = dict()
        for i in range(len(nums)):
            match_dict[nums[i]] = i
        for i in range(len(nums)):
            temp1 = target - nums[i]
            temp2 = match_dict.get(temp1)
            if temp2:
                return [i,temp2]

# GOD SOULTION
class Solution:
    def twoSum(self, nums, target):
        # """
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        # """

        hashtable = {}
        for i, num in enumerate(nums):
            if target - num in hashtable:
                return [hashtable[target - num], i]
            hashtable[num] = i
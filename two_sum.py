class Solution:
    def __init__(self):
        pass
    def twoSum1(self, nums, target):
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


    def twoSum2(self, nums, target):
        temp = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        result = [i,j]
                        return result
                    

if __name__ == '__main__':
    print(Solution().twoSum(nums = [2, 7, 11, 15], target = 9))
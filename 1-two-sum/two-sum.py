class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dictionary = {}
        for i in range (0, len(nums)):
            dictionary[nums[i]] = i
        
        print(dictionary)

        for i in range (0, len(nums)):
            num = nums[i]
            print("parto con " + str(num))
            if (target - num in dictionary and dictionary[target - num] != i):
                return i, dictionary[target - num]
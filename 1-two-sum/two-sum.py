class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums2 = list(nums)
        nums2.sort()
        print(nums2)
        sum = -1000000000000
        i = 0
        j = len(nums2) - 1
        while (sum != target):
            sum = nums2[i] + nums2[j]
            print(nums2[i], nums2[j])
            print(sum)
            if (sum < target):
                print("somma minore")
                i = i + 1
            elif (sum > target):
                print("somma maggiore")
                j = j - 1
        
        num1 = nums2[i]
        print("num1:", num1)
        num2 = nums2[j]
        print("num2:", num2)

        index1 = 0
        index2 = 0

        flag1 = False
        flag2 = False

        for i in range (0, len(nums)):
            if nums[i]== num1 and flag1 == False:
                index1 = i
                print("num1 si trova a ", index1)
                flag1 = True
                nums = nums[:i] + [-10000000000] + nums[i+1:]
                print(nums)
            if nums[i] == num2 and flag2 == False:
                index2 = i
                print("num2 si trova a " ,index2)
                flag2 = True
                nums = nums[:i] + [-1000000000000] + nums[i+1:]
                print(nums)

        return index1, index2
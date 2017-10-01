class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_of_nums = {}
        for i in range(len(nums)):
            map_of_nums[nums[i]] = i

        output_map = []
        for i in range(len(nums)):
            selection = nums[i]
            remainder = target - selection
            if remainder in map_of_nums:
                output_map = [i, map_of_nums[remainder]]
                return output_map
        return output_map


instance = Solution()

result = instance.twoSum([1,2,3,4,5], 7)
print (result)

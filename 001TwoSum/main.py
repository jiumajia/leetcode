# for commit code ###
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
                if (target-num) in nums[idx+1:]:
                    return [idx, nums[idx+1:].index(target-num)+(idx+1)]
        return []
# for commit code ###

class Solution2:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index,a in enumerate(nums):
            if target - a in nums and nums.index(target -a) != index:
                return [index,nums.index(target -a)]


if __name__ == "__main__":
    s = Solution()
    print s.twoSum([3,3], 6)

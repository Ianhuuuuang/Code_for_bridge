class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for key, value in enumerate(nums):
            ans = target - key
            nums.pop(0)
            if ans
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 26
    a = Solution().twoSum(nums,target)
    print(a)
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        No = range(len(nums))
        D = dict(zip(nums,No))
        while len(nums)>1:
            head = nums.pop(0)
            ans = target-head
            if ans in nums:
                return(D[head],D[ans])
                
if __name__ == "__main__":
    nums = [2,7,11,15]
    target = 26
    a = Solution().twoSum(nums,target)
    print(a)
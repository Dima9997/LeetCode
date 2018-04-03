class Solution:
    def arrayPairSum(self, nums):
        nums.sort()
        print(sum(nums[::2]))


solution = Solution()
solution.arrayPairSum(nums=[1, 2, 3, 4])

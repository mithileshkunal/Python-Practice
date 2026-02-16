# iven an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# The below works if the list is sorted
# solving this with two pointer left and right

class Solution:
    def twoSum(self, nums, target: int):
        left = 0
        right = len(nums) - 1
        while right > 0 and left < len(nums):
            sum = nums[left] + nums[right]
            if sum > target:
                # sum is greater, so decrease the right
                right = right - 1
            elif sum < target:
                # sum is smaller, so increase the left
                left = left + 1
            elif sum == target:
                a = [left, right]
                return a


if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([3, 5, 7, 9], 10)
    print(res)

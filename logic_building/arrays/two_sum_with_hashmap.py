# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.
# solving this with hashmap this works irrespective of it the list is sorted or not

class Solution:
    def twoSum(self, nums, target: int):
        prevDict = {}
        for index, item in enumerate(nums):
            s = target - item
            if s in prevDict:
                res = [prevDict[s], index]
                return res
            else:
                prevDict[item] = index


if __name__ == "__main__":
    sol = Solution()
    res = sol.twoSum([-1, -3, -5, -7], -10)
    print(res)

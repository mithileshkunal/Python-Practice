# https://neetcode.io/problems/duplicate-integer/question
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums) -> bool:
        counter = {}
        for item in nums:
            if item in counter:
                counter[item] = counter[item] + 1
            else:
                counter[item] = 1
            if counter[item] > 1:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    n = [1, 2, 3, 4, 5]
    print(sol.hasDuplicate(n))

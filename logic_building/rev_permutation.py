# https://codeforces.com/problemset/problem/2193/B

import logging


# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')
log = logging.getLogger(__name__)
    

class Solution:
    def get_max_permutation(self, nums):
        max_arr = self.find_max(nums)
        arr = []
        for index, item in enumerate(nums):
            arr.append((item, index))
        log.info(arr)
        current = 0
        rev_start = 0
        rev_end = -100
        while current < len(max_arr):
            log.info(f"{current}")
            if max_arr[current][1] == current:
                # This means first max is in first place etc,
                rev_start = rev_start + 1
            else:
                #code to reverse from the current item in nums
                # we got the next max
                log.info(f"{max_arr}")
                rev_end = max_arr[current][1]
                log.info(f"rev_end is {rev_end}")
                break
            current = current + 1
        log.info(f"rev_start is {rev_start} and rev_end is {rev_end}")
        result = self.rev_array(nums, rev_start, rev_end)
        log.info(f"{result}")

    def rev_array(self, nums, rev_start, rev_end):
        result = []
        if rev_start < rev_end:
            result = result + nums[0:rev_start]+nums[rev_end: rev_start - 1:-1]+nums[rev_end + 1:]
        else:
            result = nums
        return result

    def find_max(self, nums):
        for index, item in enumerate(nums):
            log.info(f"{index}, {item}")
        result = sorted([(v, i) for i, v in enumerate(nums)], reverse=True)
        log.info(result)
        return result


if __name__ == "__main__":
    ans = Solution()
    ans.get_max_permutation([2, 10, 100, -4])

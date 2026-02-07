# URL - https://leetcode.com/problems/count-monobit-integers/description/ 
# 
# 3827. Count Monobit Integers

# You are given an integer n.
# An integer is called Monobit if all bits in its binary representation are the same.
# Return the count of Monobit integers in the range [0, n] (inclusive).
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(asctime)s - %(filename)s - %(funcName)s - %(lineno)d - %(message)s')


class Solution:
    log = logging.getLogger(__name__)
    
    def get_monobits(self, n: int) -> []:
        for i in range(0, n + 1):
            self.log.debug(f"{i}: {bin(i)}")
            val = bin(i)[2:]    # get bin values exluding first two chars
            self.log.debug(f"{val}")
            if val.count('1') == len(val) or val.count('0') == len(val):
                self.log.info(f"{i}---{val}")


if __name__ == "__main__":
    Solution().get_monobits(100)

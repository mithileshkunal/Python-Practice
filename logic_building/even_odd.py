# Given a positive integer n, determine whether it is odd or even. Return true if the number is even and false if the number is odd.

class Solution:
    def isEven(self, n):
        if n % 2 == 0:
            return True
        else:
            return False


if __name__ == "__main__":
    a = int(input("Enter a number: "))
    print("{0} is Even:::{1}".format(a, Solution().isEven(a)))

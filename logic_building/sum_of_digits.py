# program to do sum of digits of a given number
def sum_of_digits(n):
    total = 0
    while n > 0:
        rem = n % 10
        total = total + rem
        # print(total, "-->")
        n = n // 10

    print("Sum is ", total)


if __name__ == "__main__":
    n = int(input("Enter a number:"))
    sum_of_digits(n)

# create a function to calculate the factorial of a number.

def factorial(num):
    result = 1
    if num == 0:
        return result
    for i in range(1, num + 1):
        result *= i
    return result


def main():
    print(factorial(6))


main()

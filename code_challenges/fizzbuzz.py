# create a function accepts two inputs 'start' and 'end'. It loops over all the numbers from start to end (excluding the end value) and adds them to a list it returns. If the number is a multiple of 3, instead of appending the number, append "fizz". If the number is a multiple of 5, instead append "buzz". If it is a multiple of 3 and 5 then instead append "fizzbuzz".


def fizzbuzz(start, end):
    result = []
    for i in range(start, end):
        res_string = ""
        if i % 3 == 0:
            res_string += "fizz"
        if i % 5 == 0:
            res_string += "buzz"
        if res_string:
            result.append(res_string)
        else:
            result.append(i)
    return result


def main():
    print(fizzbuzz(6, 9))


main()

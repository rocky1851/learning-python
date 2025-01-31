# create a function that takes a list and returns a new list with all the non-integer types removed.


def remove_nonints(nums):
    only_ints = []
    for num in nums:
        if type(num) == int:
            only_ints.append(num)
    return only_ints


def main():
    mixed_list = [True, 300, 2, False, "otherstring", 76, 86, "morestrings"]
    only_ints = remove_nonints(mixed_list)
    print(only_ints)


main()

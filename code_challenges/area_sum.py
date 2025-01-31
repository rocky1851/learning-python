# creating an area_sum() function which accepts a list of rectangles, where each rectangle is a dictionary that has the following structure:
# { "height": 5, "width": 6 }
# The function will calculate the area of each rectangle, then sum them all up and return the result.


def area_sum(rectangles):
    sum = 0
    for rectangle in rectangles:
        area = rectangle["height"] * rectangle["width"]
        sum += area
    return sum


def main():
    rectangles = [{"height": 10, "width": 11}, {"height": 12, "width": 13}]
    total_area = area_sum(rectangles)
    print(total_area)


main()

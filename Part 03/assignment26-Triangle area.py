from math import sqrt

""" Import sqtr from the math library"""

def area(a, b, c):
    
    """ Lines to identify the 3 faces of a triangle and the respective formulas to obtain perimeter and area with those values """
    perimeter = (a+b+c)
    s = (perimeter/2)
    area = sqrt((s)*(s-a)*(s-b)*(s-c))
    return area


def main():
    line_a= float(input("Enter the length of the first side: "))
    line_b = float(input("Enter the length of the second side: "))
    line_c = float(input("Enter the length of the third side: "))

    triangle_area = area(line_a, line_b, line_c)
    print(f"The triangle's area is {triangle_area:.1f}")


if __name__ == "__main__":
    main()

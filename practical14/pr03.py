class AreaCalculator:
    def print_area(self, length, breadth=None):
        if breadth is None:
            area = length ** 2  # Square's area
            print("Area of square with side {} is: {}".format(length, area))
        else:
            area = length * breadth  # Rectangle's area
            print("Area of rectangle with length {} and breadth {} is: {}".format(length, breadth, area))

# Example usage:
calculator = AreaCalculator()

# Calculate and print area of a square
calculator.print_area(5)

# Calculate and print area of a rectangle
calculator.print_area(4, 6)

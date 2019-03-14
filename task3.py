"""
===================   TASK 3   ====================
* Name: Area Of Circle
*
* Write a function `area_of_circle` that will
* return area enclosed by a circle of radius `r`.
* Consider that only float value for radius will
* be passed. Negative values should be considered
* as typo and function should ignore sign of a
* number.
*
* Note: Please describe in details possible cases
* in which your solution might not work.
*
* Use main() function to test your solution.
===================================================
"""
import math


def area_of_circle(r):
    return (abs(r)**2)*math.pi


def main():
    area = area_of_circle(-10)
    print("Area of circle is: ", area)


main()

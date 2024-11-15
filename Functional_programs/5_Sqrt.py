'''
    @Author: Ankitha B L
    @Date:10 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 10-11-2024
    @Title : Sqaure Root problem
'''
def sqrt(c):
    """Calculates the square root of a number using Newton's method.

    Args:
        c: Number to find the square root of.

    Returns:
        Square root of c.
    """

    t = c
    epsilon = 1e-15
    while abs(t - c/t) > epsilon * t:
        t = (c/t + t) / 2.0
    return t


c = float(input("Enter a number: "))
sqrt_c = sqrt(c)
print("Square root:", sqrt_c)
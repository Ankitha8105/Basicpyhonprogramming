'''
    @Author: Ankitha B L
    @Date:10 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 10-11-2024
    @Title : Monthly pay Calculation problem
'''
def monthly_payment(P, Y, R):
    """Calculates the monthly payment for a loan.

    Args:
        P: Principal amount.
        Y: Number of years.
        R: Annual interest rate.

    Returns:
        Monthly payment.
    """

    r = R / (12 * 100)
    n = 12 * Y
    return (P * r * (1 + r)**n) / ((1 + r)**n - 1)

# Example usage:
P = float(input("Enter principal P : "))
Y = float(input("Enter Year Y : "))
R = float(input("Enter Rate of intereset R : "))
payment = monthly_payment(P, Y, R)
print("Monthly payment:", payment)
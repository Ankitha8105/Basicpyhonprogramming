'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 09-11-2024
    @Title : To find Da of Week problem
'''
def day_of_week(d, m, y):
    """Calculates the day of the week for a given date.

    Args:
        d: Day of the month.
        m: Month of the year.
        y: Year.

    Returns:
        The day of the week (0 for Sunday, 1 for Monday, etc.).
    """

    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + 31 * m0 // 12) % 7

    return d0


d = int(input("Enter the Date"))
m = int(input("Enter the Month"))
y = int(input("Enter the Yeaar"))
day = day_of_week(d, m, y)
print("Day of the week:", day)
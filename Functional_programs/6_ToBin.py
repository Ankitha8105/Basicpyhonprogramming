'''
    @Author: Ankitha B L
    @Date:10 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 10-11-2024
    @Title : Decimal To Binary problem
'''
def to_binary(n):
    """Converts a decimal number to binary.

    Args:
        n: Decimal number.

    Returns:
        Binary representation of n.
    """

    binary = ""
    while (n != 0):
        binary = str(n % 2) + binary
        n //= 2

    return binary

def main():
    n = int(input("Enter a decimal number: "))
    binary_str = to_binary(n)
    print(f"Binary representation {binary_str}")

if __name__ == "__main__":
    main()
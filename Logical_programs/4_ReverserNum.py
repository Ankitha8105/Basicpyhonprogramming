
'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 2:35
    @Title : Reverse the number problem
'''
def reverse_num(num):
    """ 
    Description :
        This function is used to reverse a number
    Parameters :
        num = Number to be reversed
    Return :
        It returns the reversed number
    """
    rev = 0
    if num == 0:
        print("Please enter valid number")
    else:
        while( num != 0):
            d = num%10
            rev = rev*10 + d
            num = num//10

    return rev

def main():
    num = int(input("Enter the Number"))

    reverse = reverse_num(num)

    print(f"The Reverse of {num} is {reverse}")

if __name__ == "__main__":
    main()
'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12:23
    @Title : Power of Two Numbers problem
'''

def find_pow(num):
    """ 
    Description :
         This function is used to find power of two
    Parameters :
        num = Entered to find the power of 2
    Return :
        It returns the number power of 2 value
    """
    if(num>=0):
        pow =  2 ** num
        return pow
    else:
        print("Please Enter Correct number")

def main():
    n = int(input("Enter the number to calculate power of two "))

    power = find_pow(n)

    print(f"Number Power of Two value {power}")

if __name__ == "__main__":
    main()
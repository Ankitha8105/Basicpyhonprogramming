'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12:40
    @Title : Even Odd Number problem
'''

def num_evenorodd(n):
    """ 
    Description :
        This function is used to find number is even or odd
    Parameters :
        m = user entered number
    Return :
        It returns number is even or odd
    """
    if(n%2 == 0):
        return "Even"
    else:
        return "Odd"
    
def main():
    n = int(input("Enter the  number"))
    num = num_evenorodd(n)
    print(f"Number is {num}")

if __name__ == "__main__":
    main()
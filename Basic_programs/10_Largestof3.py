'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 01:00pm
    @Title : Largest Among Three numbers problem
'''

def larger(x,y,z):
    """ 
    Description :
        This function is used to find the largest among three numbers
    Parameters :
        x = first number
        y = second number
        z = Third number
    Return :
        It returns Largest among Three Numbers
    """
    if(x >= y and x>= z):
        big = x
    elif(y >= z):
        big = y
    else:
        big = z

    return big

def main():
    x = int(input("Enter first number"))
    y = int(input("Enter second number"))
    z = int(input("Enter Third number"))

    largest = larger(x,y,z)

    print(f"Largest among three numbers {x,y,z} is {largest}")

if __name__ == "__main__":
    main()
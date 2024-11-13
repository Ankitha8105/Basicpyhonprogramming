'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12 : 32
    @Title : Swap Two Numbers problem
'''

def swap(a,b):
    """ 
    Description :
        This function is used to swap the two numbers
    Parameters :
        m = first number
        n = second number
    Return :
        It returns swapped numbers
    """
     
    print("Before Swapping ",a,b)
    t = a
    a = b
    b = t

    '''a = a+b
        b=a-b
        a=a-b
    '''
    print("After Swapping",a,b)

def main():
    a = int(input("Enter First number :"))
    b = int(input("Enter second number :"))

    swap(a,b)

if __name__ == "__main__":
    main()
    
'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 1:13
    @Title : Fibonacci Series problem
'''

def fact_num(num):
    
    """ 
    Description :
        This function is used to find the factorial of a number
    Parameters :
        num = user entered number
    Return :
        It returns the factorial value of a number
    """
    n1 = 0
    n2 = 1
    print(n1,end= ' ')
    print(n2,end = ' ')
 
    for i in range(1,num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3

        print(n3,end=' ')

def main():
    num = int(input("Enter  the number :"))

    fact_num(num)

if __name__ == "__main__":
    main()

'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 2:20
    @Title : Prime NUmber problem
'''

def prime_num(num):
    """ 
    Description :
        This function is to check number is prime number or not
    Parameters :
        num = User entered number to check number is prime number or not
    Return :
        It returns the prime number or not
    """
    flag = True
    i = 2

    while  i<=num/2:
        if(num%i == 0):
            flag = False
            break
        i += 1

    if flag:
        return "Prime"
    else:
        return "Not Prime"
    
def main():
    num = int(input("Enter the Number :"))

    prime = prime_num(num)

    print(f" The number {num} is {prime} number")

if __name__ == "__main__":
    main()
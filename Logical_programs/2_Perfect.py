'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 01 : 20
    @Title : Perfect Number problem
'''

def perfect_num(num):
    """ 
    Description :
        This function is to check number is perfect number or not
    Parameters :
        num = User entered number to check number is perfect number or not
    Return :
        It returns the perfect number or not
    """
    if(num <= 0):
        print("Please,Enter valid Number ") 
    
    else:
        sum =0
        i=1
        while( i<= num/2 ):
            if(num%i == 0):
                sum += i
            i += 1

    if(sum == num):
        return "Perfect"
    else:
        return "Not Perfect"
    
def main():
    num = int(input("Enter the Number :"))

    number = perfect_num(num)

    print(f" The number {num} is {number}")

if __name__ == "__main__":
    main()
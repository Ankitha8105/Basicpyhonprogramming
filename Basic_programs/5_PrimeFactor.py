'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 07-11-2024
    @Title : Prime Factors problem
'''

def prime_factor(num):
    """ 
    Description :
            This function is used to find the prime factors of a number
    Parameters :
        num = Entered num to find the prime factors

    Return :
            It returns the prime factors of a number
    """
    i = 2
    while(i*i <= num ):
        flag = True

        for j in range(2,i):
            if(i%j == 0):
                flag = False
                break
       
        if flag:
            if(num%i == 0):
                return i
    
        i += 1

def main():
    num = int(input("Enter Number :"))

    factor = prime_factor(num)

    print(f" Prime Factors of {num} is {factor}")

if __name__ == "__main__":
    main()
'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12:00
    @Title : Leap Year problem
'''

def leap_year(year):

    """ 
    Description :
        This function is used user entered year is leap year or not
    Parameters :
        year = user entered year 
    Return :
        It returns the entered year is leap year or not

    """
    
    if(year>999 and year < 10000):
        if( (year%4 == 0) and (year%100 != 0 ) or (year%400 == 0 )):
            l_year = "Leap Year"
        else:
            l_year = "Not a Leap year"
        return l_year
    else:
        print("ENter valid year")

def main():
    year = int(input("Enter the Year"))
    ans = leap_year(year)
    print(f"{year} is a {ans}")

if __name__ == "__main__":
    main()
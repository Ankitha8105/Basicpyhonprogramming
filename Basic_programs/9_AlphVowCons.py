'''
    @Author: Ankitha B L
    @Date: 07-11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 12:47 pm
    @Title : Alphabet is Vowel or Constent problem
'''

def alp_voworcons(ch):
    """ 
    Description :
        This function is used to find character is vowel or consoennt
    Parameters :
        m = user entered character
    Return :
        It returns each character is vowel or consonent
    """

    if(ch=='a' or ch=='e' or ch == 'i' or ch == 'o' or ch == 'u'):
            return "vowel"
    else:
            return "Consonent"
    
def main():
    
    char = input("Enter the String :")

    alpha = alp_voworcons(char)

    print(f"The Entered character {char} is {alpha} ")

if __name__ == "__main__":
      main()
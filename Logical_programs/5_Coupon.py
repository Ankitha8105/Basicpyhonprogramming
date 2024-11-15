'''
    @Author: Ankitha B L
    @Date:09 -11-2024
    @Last Modified by: Ankitha B L
    @Last Modified time: 3:15
    @Title : To find n Distinct coupon problem
'''
import random

def generate_tickets(num_tickets):
    """Generates a specified number of unique ticket numbers.

    Args:
        num_tickets: The number of tickets to generate.

    Returns:
        A list of unique ticket numbers.
    """

    tickets = set()
    while len(tickets) < num_tickets:
        ticket_number = random.randint(1000, 10000)
        tickets.add(ticket_number)

    return list(tickets)


def generate_random(ticket,list_tickets):
    """ 
    Description :
        This function is used to generate the random numbers
    Parameters :
        ticket = Number of coupons
    Return :
        It returns the random number
    """
    random_num = set()
    while len(random_num) < ticket:
        random_num.add(random.choice(list_tickets))
    return random_num
   

def check_winner(coupon,random):
    """ 
    Description :
        This function is used to find the winner
    Parameters :
        coupon = user coupon number
        random = generated random number
    Return :
        It returns the user win the lottery or not
    """
    if(coupon in random):
        return True
    else:
        return False
                
def main():
    ticket = int(input("Enter how many lotery ticket want to generate :"))

    list_tickets = generate_tickets(ticket)

    random = generate_random(6,list_tickets)

    coupon = int(input("Enter coupon our coupon number :"))

    winner = check_winner(coupon,random)

    if winner:
        print("Congratulations! You've won the lottery!")
    else:
        print("Better luck next time")

if __name__ == "__main__":
    main()